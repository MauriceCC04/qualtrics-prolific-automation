import requests
import json

#prolific api details
# Your API configuration
API_TOKEN = ""  # Replace with your actual token
BASE_URL = "https://api.prolific.com/api/v1/"

#build qualtrics survey
# Configuration
DATACENTER_ID = ""
API_TOKEN = ""
BASE_URL = f"https://{DATACENTER_ID}.qualtrics.com/API/v3/"
HEADERS = {
    "Content-Type": "application/json",
    "X-API-TOKEN": API_TOKEN
}

def test_api_connection():
    """Test Qualtrics API connection"""
    try:
        response = requests.get(BASE_URL + "whoami", headers=HEADERS)
        response.raise_for_status()
        user_info = response.json()
        print("✓ API Connection Successful")
        print(f"User Info: {json.dumps(user_info, indent=2)}")
        return True
    except requests.exceptions.RequestException as e:
        print(f"✗ Connection Failed: {str(e)}")
        if response:
            print(f"Status Code: {response.status_code}")
            print(f"Response: {response.text}")
        return False

def create_survey(attributes, text):
    """Create a new survey with sample questions"""
    survey_payload = {
        "SurveyName": "Attribute Scoring Survey",
        "Language": "EN",
        "ProjectCategory": "CORE",
    }


    try:
        response = requests.post(
            BASE_URL + "survey-definitions",
            headers=HEADERS,
            json=survey_payload
        )
        response.raise_for_status()

        result = response.json()
        if result["meta"]["httpStatus"] == "200 - OK":
            survey_id = result["result"]["SurveyID"]
            print(f"✓ Survey created successfully!\nSurvey ID: {survey_id}")
            # Add a questions
            #add initial text:
            add_eval(survey_id, text)
            for attribute in markers_dictionary:
                print(f"\nAdding questions for attribute: {attribute}")
                add_question(survey_id, attribute)
            return survey_id
        else:
            print("✗ Survey creation failed")
            print(json.dumps(result, indent=2))
            return None

    except requests.exceptions.RequestException as e:
        print(f"✗ API Request Failed: {str(e)}")
        if response:
            print(f"Status Code: {response.status_code}")
            print(f"Response: {response.text}")
        return None

def add_eval(survey_id, text):
    """Adds a descriptive text block to the beginning of the survey."""
    question_payload = {
        "QuestionText": text,
        "DataExportTag": "eval_text",
        "QuestionType": "DB",  # Use Descriptive Text question type
        "Selector": "TB",  # Use Text Box display
        "Configuration": {
            "QuestionDescriptionOption": "UseText"
        },
        "QuestionDescription": "Evaluation Text"
    }
    try:
        response = requests.post(
            f"{BASE_URL}survey-definitions/{survey_id}/questions",
            headers=HEADERS,
            json=question_payload
        )
        response.raise_for_status()
        print("✓ Evaluation text added successfully!")
    except requests.exceptions.RequestException as e:
        print(f"✗ API Request Failed: {str(e)}")

#attributes of form: attributes = {"attribute1": ["marker1", "marker2"], "attribute2": ["marker3", "marker4"]}
#ex param = attribute 1
#must iterate through markers asking to rate the text on the markers
#then must ask to rate the attribute itself
#should be text questions

def add_text_question(survey_id, addition):
    """Adds questions to the survey based on user input."""
    question_payload = {}
    for marker in attributes[addition]:
      question_payload = {
          "QuestionText": f"Rate text on marker: {marker}",
          "DataExportTag": "Q4",
          "QuestionType": "TE",
          "Selector": "SL",
          "Configuration": {
              "QuestionDescriptionOption": "UseText"
          },
          "QuestionDescription": "Text rating on marker."
      }
      try:
          response = requests.post(
              f"{BASE_URL}survey-definitions/{survey_id}/questions",
              headers=HEADERS,
              json=question_payload
          )
          response.raise_for_status()
          print("✓ Question added successfully!")
      except requests.exceptions.RequestException as e:
          print(f"✗ API Request Failed: {str(e)}")
    #rating text based on attribute
    question_payload = {
        "QuestionText": f"Rate text on attribute: {addition}",
        "DataExportTag": "Q2",
        "QuestionType": "TE",
        "Selector": "SL",
        "Configuration": {
            "QuestionDescriptionOption": "UseText"
        },
        "QuestionDescription": "Text rating on attribute."
    }
    try:
        response = requests.post(
            f"{BASE_URL}survey-definitions/{survey_id}/questions",
            headers=HEADERS,
            json=question_payload
        )
        response.raise_for_status()
        print("✓ Question added successfully!")
    except requests.exceptions.RequestException as e:
        print(f"✗ API Request Failed: {str(e)}")

def add_question(survey_id, addition):
    """Adds questions to the survey based on user input."""
    question_payload = {}
    #choices strongly agree etc
    choice_list = ['Strongly Agree', 'Agree', 'Neutral', 'Disagree', 'Strongly Disagree']
    choices_dict = {str(i+1): {"Display": choice} for i, choice in enumerate(choice_list)}

    for marker in markers_dictionary[addition]:
      question_payload = {
          "QuestionText": f"Rate text on marker: {marker}",
          "DataExportTag": "Q4",
          "QuestionType": "MC",
          "Selector": "SAVR",
          "SubSelector": "TX",
          "Configuration": {
              "QuestionDescriptionOption": "UseText"
          },
          "QuestionDescription": "Text rating on marker."
      }
      question_payload["Choices"] = choices_dict
      question_payload["ChoiceOrder"] = list(choices_dict.keys())
      try:
          response = requests.post(
              f"{BASE_URL}survey-definitions/{survey_id}/questions",
              headers=HEADERS,
              json=question_payload
          )
          response.raise_for_status()
          print("✓ Question added successfully!")
      except requests.exceptions.RequestException as e:
          print(f"✗ API Request Failed: {str(e)}")
    #text based on attribute
    question_payload = {
        "QuestionText": f"Rate text on attribute: {addition}",
        "DataExportTag": "Q2",
        "QuestionType": "MC",
        "Selector": "SAVR",
        "SubSelector": "TX",
        "Configuration": {
            "QuestionDescriptionOption": "UseText"
        },
        "QuestionDescription": "Text rating on attribute."
    }
    question_payload["Choices"] = choices_dict
    question_payload["ChoiceOrder"] = list(choices_dict.keys())
    try:
        response = requests.post(
            f"{BASE_URL}survey-definitions/{survey_id}/questions",
            headers=HEADERS,
            json=question_payload
        )
        response.raise_for_status()
        print("✓ Question added successfully!")
    except requests.exceptions.RequestException as e:
        print(f"✗ API Request Failed: {str(e)}")

def get_survey_preview_link(survey_id):
    response = requests.get(f"{BASE_URL}/surveys/{survey_id}", headers=HEADERS)
    if response.status_code == 200:
        # This API call gives survey info, but doesn't have a direct preview link
        # The preview link follows a known pattern:
        preview_link = f"https://{DATACENTER_ID}.qualtrics.com/jfe/preview/{survey_id}"
        print(f"Preview link: {preview_link}")
        return preview_link
    else:
        print("Error retrieving survey info:", response.status_code, response.text)
        return None

def publish_and_activate(survey_id):
    # Publish the survey
    global BASE_URL # Declare BASE_URL as global to modify it within the function
    publish_url = f"{BASE_URL}/surveys/{survey_id}/publish"
    publish_response = requests.post(publish_url, headers=HEADERS)
    if publish_response.status_code == 200:
      print("Survey published successfully!")
    else:
        print("Failed to publish survey.")
        print(f"Response: {publish_response.text}")
    BASE_URL = f'https://bocconi.eu.qualtrics.com/API/v3/surveys/' # This now modifies the global BASE_URL
    url = f"{BASE_URL}{survey_id}"
    data = {
        "isActive": True
    }
    response = requests.put(url, headers=HEADERS, data=json.dumps(data))
    print(response.status_code)
    print(response.json())
    url = f"https://bocconi.eu.qualtrics.com/jfe/form/{survey_id}"
    print(url)
    return url

# Prolific API configuration
PROLIFIC_TOKEN = ""  # Replace with your actual token
PROLIFIC_URL = "https://api.prolific.com/api/v1"

# Headers for authorization
prolific_headers = {
    "Authorization": f"Token {PROLIFIC_TOKEN}",
    "Content-Type": "application/json"
}

# Function to create a study draft
def create_study_draft(survey_link):
    url = f"{PROLIFIC_URL}/studies/"
    formatted = survey_link + "?participant={{%PROLIFIC_PID%}}"
    print(formatted)
    # Basic study details
    study_data = {
        "name": "Test Study",
        "description": "This study was created as a test",
        "external_study_url": formatted,
        "prolific_id_option": "url_parameters",
        "completion_codes": [
            {
                "code": "ABC123",
                "code_type": "COMPLETED",
                "actions": [
                    {"action": "AUTOMATICALLY_APPROVE"}
                ]
            }
        ],
        "total_available_places": 5,
        "estimated_completion_time": 5,
        "reward": 50,  # This is in cents (100 = $1.00 or £1.00)
        "device_compatibility": ["desktop"],
        "peripheral_requirements": [],
        "filters": []  # No filters means available to all participants
    }

    # Make the API request
    response = requests.post(url, headers=prolific_headers, data=json.dumps(study_data))

    # Check if successful
    if response.status_code == 201:
        print("Study draft created successfully!")
        return response.json()
    else:
        print(f"Error creating study: {response.status_code}")
        print(response.text)
        return None

# Function to publish the study
def publish_study(study_id):
    url = f"{PROLIFIC_URL}/studies/{study_id}/transition/"

    publish_data = {
        "action": "PUBLISH"
    }

    response = requests.post(url, headers=prolific_headers, data=json.dumps(publish_data))

    if response.status_code == 200:
        print("Study published successfully!")
        return response.json()
    else:
        print(f"Error publishing study: {response.status_code}")
        print(response.text)
        return None

markers_dictionary = {
    "assumptions": {
        "Articulation of Assumptions": "Evaluate the clarity and precision of stated starting points/premises. Identify both explicit 'if-then' logical statements and implicit causal relationships. Assess whether key assumptions are clearly defined or open to multiple interpretations.",
        "Justification of Assumptions": "Analyze whether sufficient reasoning/evidence is provided when shared understanding cannot be assumed. Evaluate if context is appropriately provided when shared understanding can be assumed. Examine how assumptions build on each other in a logical sequence.",
        "Credibility of Assumptions": "Assess whether assumptions are reasonable given the context and audience. Examine if assumptions align with established knowledge in the field. Evaluate if alternative assumptions are acknowledged where relevant."
    },
    "problem_formulation": {
        "Identification of the Problem": "Assess whether the text clearly identifies the problem or underlying issue at hand, specifying the domain and scope of the problem. Does the text justify the scope of its analysis, including what it includes and excludes?",
        "Future State of Interest": "Evaluate whether the text articulates a clear future state of interest or desired end goal, specifying the intended outcomes and objectives in concrete terms. Does the text justify the feasibility of achieving this future end state?",
        "Contextualization": "Evaluate whether the text effectively situates the problem within its broader context,  considering historical, social, temporal, or situational factors that shape or influence the issue. Does the text explicitly connect the problem to its external environment, ensuring that the formulation is relevant and grounded?",
        "Exploration of Alternatives": "Evaluate whether the text explores alternative formulations or perspectives of the problem, evaluating the range and depth of the alternatives presented. Does the text employ systematic reasoning to compare and contrast these alternatives, identifying their strengths, weaknesses, and implications?"
    },
    "attribute_formulation": {
        "Relevance of Attributes": "Assess the relevance of the identified attributes to the strategic problem, evaluating if each attribute contributes meaningfully to the theory's practical applicability and utility in achieving the desired outcomes. Does the text justify the inclusion of each attribute, explaining its role in solving the problem or enhancing the theory's effectiveness?",
        "Completeness of Attribute Space": "Determine whether the text captures a sufficiently broad and representative space of attributes to describe the theory, including all critical attributes necessary to fully articulate the theory while avoiding gaps that might undermine its robustness. Does the text strike a balance between breadth and specificity, avoiding over-narrowing that could overly constrain the theory?",
        "Attribute Independence": "Evaluate whether the attributes are defined distinctly without unnecessary overlap or redundancy, ensuring that each attribute contributes uniquely to the theory without duplicating or conflating the roles of others. Are the attributes sufficiently independent to ensure clarity in their individual contributions?",
        "Attribute Prioritization": "Evaluate whether the text prioritizes attributes based on their expected impact or relevance to achieving the desired outcomes, distinguishing between core attributes, which are central to the theory’s success, and peripheral ones. Does it differentiate between core and peripheral attributes in terms of their significance to the theory’s outcomes?",
        "Quality of Attributes Definition": "Evaluate the quality of the attributes’ definitions, assessing whether the attributes are defined with sufficient detail to allow for verification, interpretation, or refinement through experimentation or analysis. Are the attributes described in terms of measurable or observable criteria?"
    },
    "logical_links": {
        "Logical Clarity": "Evaluate whether the logical reasoning connecting attributes is well-constructed. Do they specify conditions (e.g., 'if A happens, then B increases') that are explicitly defined and clearly articulated?",
        "No Logical Fallacies": "Evaluate whether the reasoning within the theory avoids common logical fallacies, such as circular reasoning, hasty generalizations, or false cause-effect assumptions.",
        "Robustness of Links": "Determine whether the logical links between attributes are robust under different scenarios or alternative assumptions. Are they supported by reasoning that accounts for variability?",
        "Alternative Connections": "Assess whether alternative logical connections between attributes are explored. Does the theory consider and compare competing hypotheses for its links?",
        "Testable Logical Reasoning": "Evaluate whether the text tests the logical connections between attributes, either through real-world data or conceptual reasoning."
    },
    "data_orientation": {
        "Evidence-Based Support": "Assess whether the text systematically uses data or evidence to support its claims or theory. Does it demonstrate a clear connection between the evidence presented and the arguments made?",
        "Deliberate Information Gathering": "Determine whether the text actively seeks out new and relevant information during its reasoning process, showcasing that the information-gathering  is strategic and focused on reducing uncertainty or solving the problem. Does it show a deliberate effort to explore unknowns or address gaps?",
        "Depth of Analysis": "Assess whether the text deeply analyzes the information it gathers, evaluating how well the text interprets the information it presents, connecting it meaningfully to the theory or problem. Does it go beyond surface-level data to explore patterns, implications, and nuances?",
        "Relevance of Information": "Evaluate whether the information gathered and presented is directly relevant to the theory, problem, or argument it develops. Does the text ensure that each piece of information meaningfully contributes to the argument or theory without unnecessary digressions or distractions?",
        "Breadth of Analysis": "Evaluate whether the text incorporates information from a diverse range of perspectives, disciplines, or sources to enrich its analysis. Does the text demonstrate an openness to exploring alternative explanations or methodologies, thereby enhancing the robustness and credibility of its information?"
    },
    "belief_update": {
        "Adaptability to new Information": "Evaluate the extent to which the text adapts its arguments or conclusions in response to new evidence or perspectives. Does it revise initial ideas when challenged by new data?",
        "Flexibility Without Overcorrection": "Evaluate whether the text adapts appropriately without unnecessary overcorrection. Does it strike a balance between being flexible and maintaining coherence?",
        "Adaptability of Core Assumptions": "Determine whether the text demonstrates a willingness to revise core assumptions in light of new information or contradictory evidence?"
    },
    "methodic_doubt": {
        "Uncertainty in Assumptions": "Evaluate the extent to which the text acknowledges the limitations or uncertainties associated with its assumptions. Does it openly discuss the potential impact of these uncertainties on the conclusions?",
        "Information Under Uncertainty": "Evaluate how the text approaches gathering and using information under conditions of uncertainty. Does it explicitly address limitations and explore ways to reduce uncertainty?",
        "Addressing Uncertainty in Attributes": "Assess whether the text explicitly acknowledges uncertainties in the attributes themselves. Are potential unknowns or ambiguities in their definitions and expected realizations addressed?",
        "Uncertainty in Logical Links": "Evaluate whether the theory accounts for uncertainties in logical links. Are limitations and potential variabilities in the connections acknowledged and addressed?",
        "Acknowledgment of Scope": "Assess whether the text explicitly identifies unresolved issues or areas requiring further exploration. Does the text display awareness of the limits of its own knowledge or reasoning?"
    }
}

if test_api_connection():
      print("\nCreating survey...")
      survey_id = create_survey(markers_dictionary, eval)
if survey_id:
    link = publish_and_activate(survey_id)
    #prolific
    study = create_study_draft(link)
    if study:
        # If draft created successfully, get the ID and publish
        study_id = study["id"]
        print(f"Created draft study with ID: {study_id}")
        # Uncomment the next line when you're ready to publish
        published_study = publish_study(study_id)
