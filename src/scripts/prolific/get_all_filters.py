import requests
import json
import csv
import os
from datetime import datetime

# Your API configuration
API_TOKEN = ""  # Replace with your actual token
BASE_URL = "https://api.prolific.com/api/v1"

# Headers for authorization
headers = {
    "Authorization": f"Token {API_TOKEN}",
    "Content-Type": "application/json"
}


def fetch_all_filters(workspace_id=None):
    """
    Fetch all available filters from the Prolific API

    Args:
        workspace_id (str, optional): Specific workspace ID to get contextual filters

    Returns:
        dict: The complete response with all filters
    """
    try:
        url = f"{BASE_URL}/filters/"
        params = {}

        # Add workspace_id if provided (for contextual filters like participant groups)
        if workspace_id:
            params['workspace_id'] = workspace_id

        # Add detailed=true to get more information about each filter
        params['detailed'] = 'true'

        print(f"Fetching filters from {url}...")
        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            print("Successfully fetched filters!")
            return response.json()
        else:
            print(f"Error fetching filters: {response.status_code}")
            print(response.text)
            return None
    except Exception as e:
        print(f"Exception fetching filters: {str(e)}")
        return None


def export_filters_to_json(filters_data, filename="prolific_filters.json"):
    """
    Export filters data to a JSON file

    Args:
        filters_data (dict): The filters data to export
        filename (str): The filename to save to
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(filters_data, f, indent=2)
        print(f"Filters exported to {filename}")
    except Exception as e:
        print(f"Error exporting to JSON: {str(e)}")


def export_filters_to_csv(filters_data, filename="prolific_filters.csv"):
    """
    Export filters data to a CSV file for easy viewing in spreadsheets

    Args:
        filters_data (dict): The filters data to export
        filename (str): The filename to save to
    """
    try:
        # Extract the filters array
        filters = filters_data.get('results', [])

        if not filters:
            print("No filters found to export to CSV.")
            return

        # Determine fields to export
        fieldnames = [
            'filter_id', 'title', 'description', 'type', 'data_type',
            'category', 'subcategory', 'question'
        ]

        # Special fields for select filters
        select_extra_fields = ['available_choices']

        # Special fields for range filters
        range_extra_fields = ['min_value', 'max_value']

        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames + select_extra_fields + range_extra_fields)
            writer.writeheader()

            for filter_item in filters:
                # Create a row with common fields
                row = {field: filter_item.get(field, '') for field in fieldnames if field in filter_item}

                # Add extra information based on filter type
                if filter_item.get('type') == 'select' and 'choices' in filter_item:
                    # For select filters, include available choices
                    choices = filter_item.get('choices', {})
                    row['available_choices'] = ', '.join([f"{k}:{v}" for k, v in choices.items()])

                elif filter_item.get('type') == 'range':
                    # For range filters, include min/max values
                    row['min_value'] = filter_item.get('min', '')
                    row['max_value'] = filter_item.get('max', '')

                writer.writerow(row)

        print(f"Filters exported to {filename}")
    except Exception as e:
        print(f"Error exporting to CSV: {str(e)}")


def create_filter_examples_file(filters_data, filename="filter_examples.py"):
    """
    Create a Python file with example code for using each filter

    Args:
        filters_data (dict): The filters data to process
        filename (str): The filename to save to
    """
    try:
        # Extract the filters array
        filters = filters_data.get('results', [])

        if not filters:
            print("No filters found to create examples.")
            return

        with open(filename, 'w', encoding='utf-8') as f:
            # Write file header
            f.write("# Prolific Filter Examples\n")
            f.write("# Generated on " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
            f.write("# This file contains examples of how to use Prolific filters in your API calls\n\n")

            f.write("# Dictionary of example filter configurations\n")
            f.write("filter_examples = {\n")

            for filter_item in filters:
                filter_id = filter_item.get('filter_id')
                title = filter_item.get('title')
                filter_type = filter_item.get('type')

                f.write(f"    # {title}\n")
                f.write(f"    '{filter_id}': {{\n")

                if filter_type == 'select':
                    # Example for select filters
                    choices = filter_item.get('choices', {})
                    choice_items = list(choices.items())
                    # Use the first two choices as examples, or fewer if not enough
                    example_choices = choice_items[:min(2, len(choice_items))]

                    f.write("        # Select filter example\n")
                    f.write("        'example': {\n")
                    f.write(f"            'filter_id': '{filter_id}',\n")
                    f.write("            'selected_values': [\n")
                    for key, value in example_choices:
                        f.write(f"                '{key}',  # {value}\n")
                    f.write("            ]\n")
                    f.write("        },\n")

                    # Add weighting example for select filters
                    if example_choices:
                        f.write("        # Select filter with weightings example\n")
                        f.write("        'weighted_example': {\n")
                        f.write(f"            'filter_id': '{filter_id}',\n")
                        f.write("            'selected_values': [\n")
                        for key, value in example_choices:
                            f.write(f"                '{key}',  # {value}\n")
                        f.write("            ],\n")
                        f.write("            'weightings': {\n")
                        for key, value in example_choices:
                            f.write(f"                '{key}': 1,  # Equal weighting for {value}\n")
                        f.write("            }\n")
                        f.write("        },\n")

                elif filter_type == 'range':
                    # Example for range filters
                    min_val = filter_item.get('min', '')
                    max_val = filter_item.get('max', '')
                    data_type = filter_item.get('data_type', 'integer')

                    # Format values based on data type
                    if data_type == 'date':
                        min_str = f"'{min_val}'"
                        max_str = f"'{max_val}'"
                    else:  # integer or other
                        min_str = str(min_val)
                        max_str = str(max_val)

                    f.write("        # Range filter example\n")
                    f.write("        'example': {\n")
                    f.write(f"            'filter_id': '{filter_id}',\n")
                    f.write("            'selected_range': {\n")
                    f.write(f"                'lower': {min_str},\n")
                    f.write(f"                'upper': {max_str}\n")
                    f.write("            }\n")
                    f.write("        },\n")

                    # Age range is the only range filter that supports weightings currently
                    if filter_id == 'age':
                        f.write("        # Age range filter with weightings example\n")
                        f.write("        'weighted_example': {\n")
                        f.write(f"            'filter_id': '{filter_id}',\n")
                        f.write("            'selected_range': {\n")
                        f.write(f"                'lower': {min_str},\n")
                        f.write(f"                'upper': {max_str}\n")
                        f.write("            },\n")
                        f.write("            'weightings': {\n")
                        f.write("                '0': {\n")
                        f.write("                    'selected_range': {\n")
                        f.write("                        'lower': 18,\n")
                        f.write("                        'upper': 30\n")
                        f.write("                    },\n")
                        f.write("                    'weighting': 1\n")
                        f.write("                },\n")
                        f.write("                '1': {\n")
                        f.write("                    'selected_range': {\n")
                        f.write("                        'lower': 31,\n")
                        f.write("                        'upper': 50\n")
                        f.write("                    },\n")
                        f.write("                    'weighting': 1\n")
                        f.write("                }\n")
                        f.write("            }\n")
                        f.write("        },\n")

                f.write("    },\n\n")

            f.write("}\n\n")

            # Add usage examples
            f.write("# Example of how to use these filters in a study creation:\n")
            f.write("'''\n")
            f.write("study_data = {\n")
            f.write("    \"name\": \"My Study with Filters\",\n")
            f.write("    ...\n")
            f.write("    \"filters\": [\n")
            f.write("        filter_examples['age']['example'],\n")
            f.write("        filter_examples['handedness']['example']\n")
            f.write("    ]\n")
            f.write("}\n")
            f.write("'''\n")

        print(f"Filter examples exported to {filename}")
    except Exception as e:
        print(f"Error creating examples file: {str(e)}")


def main(workspace_id=None):
    # Create an output directory
    output_dir = "prolific_filters_" + datetime.now().strftime("%Y%m%d")
    try:
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        print(f"Created output directory: {output_dir}")
    except Exception as e:
        print(f"Error creating output directory: {str(e)}")
        output_dir = "."  # Use current directory if creating the new one fails

    # Fetch filters
    filters_data = fetch_all_filters(workspace_id)

    if filters_data:
        # Export to different formats
        export_filters_to_json(filters_data, os.path.join(output_dir, "prolific_filters.json"))
        export_filters_to_csv(filters_data, os.path.join(output_dir, "prolific_filters.csv"))
        create_filter_examples_file(filters_data, os.path.join(output_dir, "filter_examples.py"))
        print("\nFilter export completed successfully!")
        print(f"All files saved to {output_dir}")
    else:
        print("\nFilter export failed due to errors fetching the filter data.")


if __name__ == "__main__":
    # You can optionally specify a workspace_id for contextual filters
    # main(workspace_id="YOUR_WORKSPACE_ID")
    main()
