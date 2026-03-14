# Prolific Filter Examples
# Generated on 2025-04-13 08:20:15
# This file contains examples of how to use Prolific filters in your API calls

# Dictionary of example filter configurations
filter_examples = {
    # Month of birth of youngest child
    'month-of-birth-of-youngest-child': {
        # Select filter example
        'example': {
            'filter_id': 'month-of-birth-of-youngest-child',
            'selected_values': [
                '0',  # Rather not say
                '1',  # January
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'month-of-birth-of-youngest-child',
            'selected_values': [
                '0',  # Rather not say
                '1',  # January
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Rather not say
                '1': 1,  # Equal weighting for January
            }
        },
    },

    # Jury duty
    'jury-duty': {
        # Select filter example
        'example': {
            'filter_id': 'jury-duty',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'jury-duty',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Hearing difficulties
    'hearing-difficulties': {
        # Select filter example
        'example': {
            'filter_id': 'hearing-difficulties',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'hearing-difficulties',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Clothing online
    'clothing-online': {
        # Select filter example
        'example': {
            'filter_id': 'clothing-online',
            'selected_values': [
                '0',  # More than once a week
                '1',  # About once per week
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'clothing-online',
            'selected_values': [
                '0',  # More than once a week
                '1',  # About once per week
            ],
            'weightings': {
                '0': 1,  # Equal weighting for More than once a week
                '1': 1,  # Equal weighting for About once per week
            }
        },
    },

    # Political Party Affiliation UK
    'political-party-affiliation-uk': {
        # Select filter example
        'example': {
            'filter_id': 'political-party-affiliation-uk',
            'selected_values': [
                '0',  # Labour
                '1',  # Conservative
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'political-party-affiliation-uk',
            'selected_values': [
                '0',  # Labour
                '1',  # Conservative
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Labour
                '1': 1,  # Equal weighting for Conservative
            }
        },
    },

    # Undergraduate year of study
    'undergraduate-year-of-study': {
        # Select filter example
        'example': {
            'filter_id': 'undergraduate-year-of-study',
            'selected_values': [
                '0',  # 1st Year
                '1',  # 2nd Year
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'undergraduate-year-of-study',
            'selected_values': [
                '0',  # 1st Year
                '1',  # 2nd Year
            ],
            'weightings': {
                '0': 1,  # Equal weighting for 1st Year
                '1': 1,  # Equal weighting for 2nd Year
            }
        },
    },

    # Quit smoking
    'quit-smoking': {
        # Select filter example
        'example': {
            'filter_id': 'quit-smoking',
            'selected_values': [
                '0',  # Currently trying to quit smoking (i.e. within the last month)
                '1',  # 1-3 months ago
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'quit-smoking',
            'selected_values': [
                '0',  # Currently trying to quit smoking (i.e. within the last month)
                '1',  # 1-3 months ago
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Currently trying to quit smoking (i.e. within the last month)
                '1': 1,  # Equal weighting for 1-3 months ago
            }
        },
    },

    # U.S. Political Affiliation
    'us-political-affiliation': {
        # Select filter example
        'example': {
            'filter_id': 'us-political-affiliation',
            'selected_values': [
                '0',  # Democrat
                '1',  # Republican
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'us-political-affiliation',
            'selected_values': [
                '0',  # Democrat
                '1',  # Republican
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Democrat
                '1': 1,  # Equal weighting for Republican
            }
        },
    },

    # UK General Election 2019
    'uk-general-election-2019': {
        # Select filter example
        'example': {
            'filter_id': 'uk-general-election-2019',
            'selected_values': [
                '0',  # I did not vote
                '1',  # Conservatives
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'uk-general-election-2019',
            'selected_values': [
                '0',  # I did not vote
                '1',  # Conservatives
            ],
            'weightings': {
                '0': 1,  # Equal weighting for I did not vote
                '1': 1,  # Equal weighting for Conservatives
            }
        },
    },

    # Working hours
    'working-hours': {
        # Select filter example
        'example': {
            'filter_id': 'working-hours',
            'selected_values': [
                '0',  # Regular 9-5
                '1',  # Permanent night shifts
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'working-hours',
            'selected_values': [
                '0',  # Regular 9-5
                '1',  # Permanent night shifts
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Regular 9-5
                '1': 1,  # Equal weighting for Permanent night shifts
            }
        },
    },

    # Employment Status
    'employment-status': {
        # Select filter example
        'example': {
            'filter_id': 'employment-status',
            'selected_values': [
                '0',  # Full-Time
                '1',  # Part-Time
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'employment-status',
            'selected_values': [
                '0',  # Full-Time
                '1',  # Part-Time
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Full-Time
                '1': 1,  # Equal weighting for Part-Time
            }
        },
    },

    # Participation in regular religious activities
    'participation-in-regular-religious-activities': {
        # Select filter example
        'example': {
            'filter_id': 'participation-in-regular-religious-activities',
            'selected_values': [
                '0',  # Yes. Both public and private
                '1',  # Yes. Public only
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'participation-in-regular-religious-activities',
            'selected_values': [
                '0',  # Yes. Both public and private
                '1',  # Yes. Public only
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes. Both public and private
                '1': 1,  # Equal weighting for Yes. Public only
            }
        },
    },

    # Climate Change
    'climate-change': {
        # Select filter example
        'example': {
            'filter_id': 'climate-change',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'climate-change',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Christianity Affiliation (New)
    'christianity-affiliation-new': {
        # Select filter example
        'example': {
            'filter_id': 'christianity-affiliation-new',
            'selected_values': [
                '0',  # Catholic
                '1',  # Anglican / Episcopalian
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'christianity-affiliation-new',
            'selected_values': [
                '0',  # Catholic
                '1',  # Anglican / Episcopalian
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Catholic
                '1': 1,  # Equal weighting for Anglican / Episcopalian
            }
        },
    },

    # Commute/travel to work
    'commutetravel-to-work': {
        # Select filter example
        'example': {
            'filter_id': 'commutetravel-to-work',
            'selected_values': [
                '0',  # by car
                '1',  # by bus
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'commutetravel-to-work',
            'selected_values': [
                '0',  # by car
                '1',  # by bus
            ],
            'weightings': {
                '0': 1,  # Equal weighting for by car
                '1': 1,  # Equal weighting for by bus
            }
        },
    },

    # 2016 US presidential election
    '2016-us-presidential-election': {
        # Select filter example
        'example': {
            'filter_id': '2016-us-presidential-election',
            'selected_values': [
                '0',  # Donald Trump
                '1',  # Hillary Clinton
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': '2016-us-presidential-election',
            'selected_values': [
                '0',  # Donald Trump
                '1',  # Hillary Clinton
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Donald Trump
                '1': 1,  # Equal weighting for Hillary Clinton
            }
        },
    },

    # Pain - duration
    'pain-duration': {
        # Select filter example
        'example': {
            'filter_id': 'pain-duration',
            'selected_values': [
                '0',  # 0-3 months
                '1',  # 3-6 months
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'pain-duration',
            'selected_values': [
                '0',  # 0-3 months
                '1',  # 3-6 months
            ],
            'weightings': {
                '0': 1,  # Equal weighting for 0-3 months
                '1': 1,  # Equal weighting for 3-6 months
            }
        },
    },

    # Living with family
    'living-with-family': {
        # Select filter example
        'example': {
            'filter_id': 'living-with-family',
            'selected_values': [
                '0',  # 0
                '1',  # 1
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'living-with-family',
            'selected_values': [
                '0',  # 0
                '1',  # 1
            ],
            'weightings': {
                '0': 1,  # Equal weighting for 0
                '1': 1,  # Equal weighting for 1
            }
        },
    },

    # Smoking frequency
    'smoking-frequency': {
        # Select filter example
        'example': {
            'filter_id': 'smoking-frequency',
            'selected_values': [
                '0',  # Less than 4 times a month
                '1',  # 1-6 times a week
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'smoking-frequency',
            'selected_values': [
                '0',  # Less than 4 times a month
                '1',  # 1-6 times a week
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Less than 4 times a month
                '1': 1,  # Equal weighting for 1-6 times a week
            }
        },
    },

    # Relationship/Marital status
    'relationshipmarital-status': {
        # Select filter example
        'example': {
            'filter_id': 'relationshipmarital-status',
            'selected_values': [
                '0',  # Single
                '1',  # In a relationship
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'relationshipmarital-status',
            'selected_values': [
                '0',  # Single
                '1',  # In a relationship
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Single
                '1': 1,  # Equal weighting for In a relationship
            }
        },
    },

    # Property Ownership
    'property-ownership': {
        # Select filter example
        'example': {
            'filter_id': 'property-ownership',
            'selected_values': [
                '0',  # I own the property I live in
                '1',  # I live in privately rented accommodation
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'property-ownership',
            'selected_values': [
                '0',  # I own the property I live in
                '1',  # I live in privately rented accommodation
            ],
            'weightings': {
                '0': 1,  # Equal weighting for I own the property I live in
                '1': 1,  # Equal weighting for I live in privately rented accommodation
            }
        },
    },

    # Tweeting Frequency
    'tweeting-frequency': {
        # Select filter example
        'example': {
            'filter_id': 'tweeting-frequency',
            'selected_values': [
                '0',  # 0 times
                '1',  # 1-3 times
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'tweeting-frequency',
            'selected_values': [
                '0',  # 0 times
                '1',  # 1-3 times
            ],
            'weightings': {
                '0': 1,  # Equal weighting for 0 times
                '1': 1,  # Equal weighting for 1-3 times
            }
        },
    },

    # Job Seeking
    'job-seeking': {
        # Select filter example
        'example': {
            'filter_id': 'job-seeking',
            'selected_values': [
                '0',  # I am currently actively looking for a job
                '1',  # I am currently not actively looking for a job
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'job-seeking',
            'selected_values': [
                '0',  # I am currently actively looking for a job
                '1',  # I am currently not actively looking for a job
            ],
            'weightings': {
                '0': 1,  # Equal weighting for I am currently actively looking for a job
                '1': 1,  # Equal weighting for I am currently not actively looking for a job
            }
        },
    },

    # Year of birth of youngest child
    'year-of-birth-of-youngest-child': {
        # Select filter example
        'example': {
            'filter_id': 'year-of-birth-of-youngest-child',
            'selected_values': [
                '0',  # Rather not say
                '1',  # 1900
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'year-of-birth-of-youngest-child',
            'selected_values': [
                '0',  # Rather not say
                '1',  # 1900
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Rather not say
                '1': 1,  # Equal weighting for 1900
            }
        },
    },

    # Webcam
    'webcam': {
        # Select filter example
        'example': {
            'filter_id': 'webcam',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'webcam',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Household Income (USD) [US participants only]
    'household-income-usd-us-participants-only': {
        # Select filter example
        'example': {
            'filter_id': 'household-income-usd-us-participants-only',
            'selected_values': [
                '0',  # Less than $10000
                '1',  # $10000–$15999
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'household-income-usd-us-participants-only',
            'selected_values': [
                '0',  # Less than $10000
                '1',  # $10000–$15999
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Less than $10000
                '1': 1,  # Equal weighting for $10000–$15999
            }
        },
    },

    # Political Spectrum (US)
    'political-spectrum-us': {
        # Select filter example
        'example': {
            'filter_id': 'political-spectrum-us',
            'selected_values': [
                '0',  # Conservative
                '1',  # Moderate
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'political-spectrum-us',
            'selected_values': [
                '0',  # Conservative
                '1',  # Moderate
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Conservative
                '1': 1,  # Equal weighting for Moderate
            }
        },
    },

    # Experience with musical instruments
    'experience-with-musical-instruments': {
        # Select filter example
        'example': {
            'filter_id': 'experience-with-musical-instruments',
            'selected_values': [
                '0',  # No. I don't play a musical instrument
                '1',  # Yes. For 0-1 years.
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'experience-with-musical-instruments',
            'selected_values': [
                '0',  # No. I don't play a musical instrument
                '1',  # Yes. For 0-1 years.
            ],
            'weightings': {
                '0': 1,  # Equal weighting for No. I don't play a musical instrument
                '1': 1,  # Equal weighting for Yes. For 0-1 years.
            }
        },
    },

    # Highest education level completed
    'highest-education-level-completed': {
        # Select filter example
        'example': {
            'filter_id': 'highest-education-level-completed',
            'selected_values': [
                '0',  # No formal qualifications
                '1',  # Secondary education (e.g. GED/GCSE)
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'highest-education-level-completed',
            'selected_values': [
                '0',  # No formal qualifications
                '1',  # Secondary education (e.g. GED/GCSE)
            ],
            'weightings': {
                '0': 1,  # Equal weighting for No formal qualifications
                '1': 1,  # Equal weighting for Secondary education (e.g. GED/GCSE)
            }
        },
    },

    # Multiple sclerosis
    'multiple-sclerosis': {
        # Select filter example
        'example': {
            'filter_id': 'multiple-sclerosis',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'multiple-sclerosis',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Current education level
    'current-education-level': {
        # Select filter example
        'example': {
            'filter_id': 'current-education-level',
            'selected_values': [
                '0',  # Secondary education (e.g. GED/GCSE)
                '1',  # High school diploma/A-levels
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'current-education-level',
            'selected_values': [
                '0',  # Secondary education (e.g. GED/GCSE)
                '1',  # High school diploma/A-levels
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Secondary education (e.g. GED/GCSE)
                '1': 1,  # Equal weighting for High school diploma/A-levels
            }
        },
    },

    # COVID-19 Employment Status
    'covid-19-employment-status': {
        # Select filter example
        'example': {
            'filter_id': 'covid-19-employment-status',
            'selected_values': [
                '0',  # I was working full-time, and am now still working or being paid for full-time hours.
                '1',  # I was working full-time, but am now working or being paid for part-time hours.
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'covid-19-employment-status',
            'selected_values': [
                '0',  # I was working full-time, and am now still working or being paid for full-time hours.
                '1',  # I was working full-time, but am now working or being paid for part-time hours.
            ],
            'weightings': {
                '0': 1,  # Equal weighting for I was working full-time, and am now still working or being paid for full-time hours.
                '1': 1,  # Equal weighting for I was working full-time, but am now working or being paid for part-time hours.
            }
        },
    },

    # COVID-19 Symptoms
    'covid-19-symptoms': {
        # Select filter example
        'example': {
            'filter_id': 'covid-19-symptoms',
            'selected_values': [
                '0',  # I have been officially diagnosed with COVID-19 (tested by a licensed medical professional), and was treated in a hospital.
                '1',  # I have been officially diagnosed with COVID-19 (tested by a licensed medical professional), and stayed at home during my recovery.
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'covid-19-symptoms',
            'selected_values': [
                '0',  # I have been officially diagnosed with COVID-19 (tested by a licensed medical professional), and was treated in a hospital.
                '1',  # I have been officially diagnosed with COVID-19 (tested by a licensed medical professional), and stayed at home during my recovery.
            ],
            'weightings': {
                '0': 1,  # Equal weighting for I have been officially diagnosed with COVID-19 (tested by a licensed medical professional), and was treated in a hospital.
                '1': 1,  # Equal weighting for I have been officially diagnosed with COVID-19 (tested by a licensed medical professional), and stayed at home during my recovery.
            }
        },
    },

    # VR headset (frequency)
    'vr-headset-frequency': {
        # Select filter example
        'example': {
            'filter_id': 'vr-headset-frequency',
            'selected_values': [
                '0',  # 0 times
                '1',  # 1-5 times
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'vr-headset-frequency',
            'selected_values': [
                '0',  # 0 times
                '1',  # 1-5 times
            ],
            'weightings': {
                '0': 1,  # Equal weighting for 0 times
                '1': 1,  # Equal weighting for 1-5 times
            }
        },
    },

    # VR headset (ownership)
    'vr-headset-ownership': {
        # Select filter example
        'example': {
            'filter_id': 'vr-headset-ownership',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'vr-headset-ownership',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # 2020 US presidential election
    '2020-us-presidential-election': {
        # Select filter example
        'example': {
            'filter_id': '2020-us-presidential-election',
            'selected_values': [
                '0',  # Joe Biden
                '1',  # Donald Trump
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': '2020-us-presidential-election',
            'selected_values': [
                '0',  # Joe Biden
                '1',  # Donald Trump
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Joe Biden
                '1': 1,  # Equal weighting for Donald Trump
            }
        },
    },

    # COVID-19 Vaccine Opinions
    'covid-19-vaccine-opinions': {
        # Select filter example
        'example': {
            'filter_id': 'covid-19-vaccine-opinions',
            'selected_values': [
                '0',  # For (I feel positively about the vaccines)
                '1',  # Against (I feel negatively about the vaccines)
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'covid-19-vaccine-opinions',
            'selected_values': [
                '0',  # For (I feel positively about the vaccines)
                '1',  # Against (I feel negatively about the vaccines)
            ],
            'weightings': {
                '0': 1,  # Equal weighting for For (I feel positively about the vaccines)
                '1': 1,  # Equal weighting for Against (I feel negatively about the vaccines)
            }
        },
    },

    # COVID-19 Vaccination
    'covid-19-vaccination': {
        # Select filter example
        'example': {
            'filter_id': 'covid-19-vaccination',
            'selected_values': [
                '0',  # Yes (at least one dose)
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'covid-19-vaccination',
            'selected_values': [
                '0',  # Yes (at least one dose)
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes (at least one dose)
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Company type
    'company-type': {
        # Select filter example
        'example': {
            'filter_id': 'company-type',
            'selected_values': [
                '0',  # Micro enterprise
                '1',  # Small and medium-sized enterprises (SME)
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'company-type',
            'selected_values': [
                '0',  # Micro enterprise
                '1',  # Small and medium-sized enterprises (SME)
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Micro enterprise
                '1': 1,  # Equal weighting for Small and medium-sized enterprises (SME)
            }
        },
    },

    # Years lived in current country of residence
    'years-lived-in-current-country-of-residence': {
        # Select filter example
        'example': {
            'filter_id': 'years-lived-in-current-country-of-residence',
            'selected_values': [
                '0',  # Less than 1 year
                '1',  # Between 1 and 2 years
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'years-lived-in-current-country-of-residence',
            'selected_values': [
                '0',  # Less than 1 year
                '1',  # Between 1 and 2 years
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Less than 1 year
                '1': 1,  # Equal weighting for Between 1 and 2 years
            }
        },
    },

    # Cochlear implant
    'cochlear-implant': {
        # Select filter example
        'example': {
            'filter_id': 'cochlear-implant',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'cochlear-implant',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Gender
    'gender': {
        # Select filter example
        'example': {
            'filter_id': 'gender',
            'selected_values': [
                '0',  # Man (including Trans Male/Trans Man)
                '1',  # Woman (including Trans Female/Trans Woman)
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'gender',
            'selected_values': [
                '0',  # Man (including Trans Male/Trans Man)
                '1',  # Woman (including Trans Female/Trans Woman)
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Man (including Trans Male/Trans Man)
                '1': 1,  # Equal weighting for Woman (including Trans Female/Trans Woman)
            }
        },
    },

    # Cisgender and Transgender
    'cisgender-and-transgender': {
        # Select filter example
        'example': {
            'filter_id': 'cisgender-and-transgender',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'cisgender-and-transgender',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Cryptocurrency
    'cryptocurrency': {
        # Select filter example
        'example': {
            'filter_id': 'cryptocurrency',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'cryptocurrency',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Cell Phone Service [US participants only]
    'cell-phone-service-us-participants-only': {
        # Select filter example
        'example': {
            'filter_id': 'cell-phone-service-us-participants-only',
            'selected_values': [
                '0',  # T-Mobile
                '1',  # Verizon
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'cell-phone-service-us-participants-only',
            'selected_values': [
                '0',  # T-Mobile
                '1',  # Verizon
            ],
            'weightings': {
                '0': 1,  # Equal weighting for T-Mobile
                '1': 1,  # Equal weighting for Verizon
            }
        },
    },

    # Mobile Phone Service [UK participants only]
    'mobile-phone-service-uk-participants-only': {
        # Select filter example
        'example': {
            'filter_id': 'mobile-phone-service-uk-participants-only',
            'selected_values': [
                '0',  # EE
                '1',  # BT Mobile
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'mobile-phone-service-uk-participants-only',
            'selected_values': [
                '0',  # EE
                '1',  # BT Mobile
            ],
            'weightings': {
                '0': 1,  # Equal weighting for EE
                '1': 1,  # Equal weighting for BT Mobile
            }
        },
    },

    # Home Internet Provider U.K
    'home-internet-provider-uk': {
        # Select filter example
        'example': {
            'filter_id': 'home-internet-provider-uk',
            'selected_values': [
                '0',  # A&A
                '1',  # Airband
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'home-internet-provider-uk',
            'selected_values': [
                '0',  # A&A
                '1',  # Airband
            ],
            'weightings': {
                '0': 1,  # Equal weighting for A&A
                '1': 1,  # Equal weighting for Airband
            }
        },
    },

    # Home Internet Provider U.S.
    'home-internet-provider-us': {
        # Select filter example
        'example': {
            'filter_id': 'home-internet-provider-us',
            'selected_values': [
                '0',  # Allo
                '1',  # Armstrong
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'home-internet-provider-us',
            'selected_values': [
                '0',  # Allo
                '1',  # Armstrong
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Allo
                '1': 1,  # Equal weighting for Armstrong
            }
        },
    },

    # Colourblindness
    'colourblindness': {
        # Select filter example
        'example': {
            'filter_id': 'colourblindness',
            'selected_values': [
                '0',  # Yes, I'm colourblind
                '1',  # No, I have no issues seeing colours
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'colourblindness',
            'selected_values': [
                '0',  # Yes, I'm colourblind
                '1',  # No, I have no issues seeing colours
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes, I'm colourblind
                '1': 1,  # Equal weighting for No, I have no issues seeing colours
            }
        },
    },

    # Boycotting
    'boycotting': {
        # Select filter example
        'example': {
            'filter_id': 'boycotting',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'boycotting',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Neurodiversity
    'neurodiversity': {
        # Select filter example
        'example': {
            'filter_id': 'neurodiversity',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'neurodiversity',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Team/Individual Sport
    'teamindividual-sport': {
        # Select filter example
        'example': {
            'filter_id': 'teamindividual-sport',
            'selected_values': [
                '0',  # I actively take part in team sports only
                '1',  # I actively take part in non-team sports only (e.g. going to the gym)
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'teamindividual-sport',
            'selected_values': [
                '0',  # I actively take part in team sports only
                '1',  # I actively take part in non-team sports only (e.g. going to the gym)
            ],
            'weightings': {
                '0': 1,  # Equal weighting for I actively take part in team sports only
                '1': 1,  # Equal weighting for I actively take part in non-team sports only (e.g. going to the gym)
            }
        },
    },

    # Retirement Plan
    'retirement-plan': {
        # Select filter example
        'example': {
            'filter_id': 'retirement-plan',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'retirement-plan',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Record Audio
    'record-audio': {
        # Select filter example
        'example': {
            'filter_id': 'record-audio',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'record-audio',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Household bill paying
    'household-bill-paying': {
        # Select filter example
        'example': {
            'filter_id': 'household-bill-paying',
            'selected_values': [
                '0',  # Yes - solely responsible
                '1',  # Yes - jointly responsible
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'household-bill-paying',
            'selected_values': [
                '0',  # Yes - solely responsible
                '1',  # Yes - jointly responsible
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes - solely responsible
                '1': 1,  # Equal weighting for Yes - jointly responsible
            }
        },
    },

    # LGBTQ+
    'lgbtq': {
        # Select filter example
        'example': {
            'filter_id': 'lgbtq',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'lgbtq',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Participating together with a friend on Prolific
    'participating-together-with-a-friend-on-prolific': {
        # Select filter example
        'example': {
            'filter_id': 'participating-together-with-a-friend-on-prolific',
            'selected_values': [
                '0',  # Yes, I have a friend who has a Prolific account and we would be willing to take part as a pair
                '1',  # No, I either do not have a friend on Prolific or we would not be willing to take part as a pair
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'participating-together-with-a-friend-on-prolific',
            'selected_values': [
                '0',  # Yes, I have a friend who has a Prolific account and we would be willing to take part as a pair
                '1',  # No, I either do not have a friend on Prolific or we would not be willing to take part as a pair
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes, I have a friend who has a Prolific account and we would be willing to take part as a pair
                '1': 1,  # Equal weighting for No, I either do not have a friend on Prolific or we would not be willing to take part as a pair
            }
        },
    },

    # EV Charging
    'ev-charging': {
        # Select filter example
        'example': {
            'filter_id': 'ev-charging',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'ev-charging',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Military veteran
    'military-veteran': {
        # Select filter example
        'example': {
            'filter_id': 'military-veteran',
            'selected_values': [
                '0',  # I'm a US services veteran
                '1',  # I'm a UK services veteran
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'military-veteran',
            'selected_values': [
                '0',  # I'm a US services veteran
                '1',  # I'm a UK services veteran
            ],
            'weightings': {
                '0': 1,  # Equal weighting for I'm a US services veteran
                '1': 1,  # Equal weighting for I'm a UK services veteran
            }
        },
    },

    # Depression
    'depression': {
        # Select filter example
        'example': {
            'filter_id': 'depression',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'depression',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Anxiety
    'anxiety': {
        # Select filter example
        'example': {
            'filter_id': 'anxiety',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'anxiety',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # ADD/ADHD
    'addadhd': {
        # Select filter example
        'example': {
            'filter_id': 'addadhd',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'addadhd',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Place of most time spent before turning 18
    'place-of-most-time-spent-before-turning-18': {
        # Select filter example
        'example': {
            'filter_id': 'place-of-most-time-spent-before-turning-18',
            'selected_values': [
                '0',  # Afghanistan
                '1',  # Aland Islands
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'place-of-most-time-spent-before-turning-18',
            'selected_values': [
                '0',  # Afghanistan
                '1',  # Aland Islands
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Afghanistan
                '1': 1,  # Equal weighting for Aland Islands
            }
        },
    },

    # Further educational study
    'further-educational-study': {
        # Select filter example
        'example': {
            'filter_id': 'further-educational-study',
            'selected_values': [
                '0',  # Undergraduate Degree
                '1',  # Master's Degree
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'further-educational-study',
            'selected_values': [
                '0',  # Undergraduate Degree
                '1',  # Master's Degree
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Undergraduate Degree
                '1': 1,  # Equal weighting for Master's Degree
            }
        },
    },

    # Interest in studying abroad
    'interest-in-studying-abroad': {
        # Select filter example
        'example': {
            'filter_id': 'interest-in-studying-abroad',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'interest-in-studying-abroad',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Oral Contraceptives
    'oral-contraceptives': {
        # Select filter example
        'example': {
            'filter_id': 'oral-contraceptives',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'oral-contraceptives',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Business Role
    'business-role': {
        # Select filter example
        'example': {
            'filter_id': 'business-role',
            'selected_values': [
                '0',  # Financial advisor (at a wealth management firm)
                '1',  # PR & Corporate Communications professional (including PR Agency staff)
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'business-role',
            'selected_values': [
                '0',  # Financial advisor (at a wealth management firm)
                '1',  # PR & Corporate Communications professional (including PR Agency staff)
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Financial advisor (at a wealth management firm)
                '1': 1,  # Equal weighting for PR & Corporate Communications professional (including PR Agency staff)
            }
        },
    },

    # COVID-19 Vaccination History
    'covid-19-vaccination-history': {
        # Select filter example
        'example': {
            'filter_id': 'covid-19-vaccination-history',
            'selected_values': [
                '0',  # 4+
                '1',  # 3
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'covid-19-vaccination-history',
            'selected_values': [
                '0',  # 4+
                '1',  # 3
            ],
            'weightings': {
                '0': 1,  # Equal weighting for 4+
                '1': 1,  # Equal weighting for 3
            }
        },
    },

    # Highest level of education completed by parents
    'highest-level-of-education-completed-by-parents': {
        # Select filter example
        'example': {
            'filter_id': 'highest-level-of-education-completed-by-parents',
            'selected_values': [
                '0',  # No formal qualifications
                '1',  # Secondary education (e.g. GED/GCSE)
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'highest-level-of-education-completed-by-parents',
            'selected_values': [
                '0',  # No formal qualifications
                '1',  # Secondary education (e.g. GED/GCSE)
            ],
            'weightings': {
                '0': 1,  # Equal weighting for No formal qualifications
                '1': 1,  # Equal weighting for Secondary education (e.g. GED/GCSE)
            }
        },
    },

    # Universal Credit
    'universal-credit': {
        # Select filter example
        'example': {
            'filter_id': 'universal-credit',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'universal-credit',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Company size
    'company-size': {
        # Select filter example
        'example': {
            'filter_id': 'company-size',
            'selected_values': [
                '0',  # 1-9
                '1',  # 10-49
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'company-size',
            'selected_values': [
                '0',  # 1-9
                '1',  # 10-49
            ],
            'weightings': {
                '0': 1,  # Equal weighting for 1-9
                '1': 1,  # Equal weighting for 10-49
            }
        },
    },

    # Blood type
    'blood-type': {
        # Select filter example
        'example': {
            'filter_id': 'blood-type',
            'selected_values': [
                '0',  # A RhD positive (A+)
                '1',  # A RhD negative (A-)
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'blood-type',
            'selected_values': [
                '0',  # A RhD positive (A+)
                '1',  # A RhD negative (A-)
            ],
            'weightings': {
                '0': 1,  # Equal weighting for A RhD positive (A+)
                '1': 1,  # Equal weighting for A RhD negative (A-)
            }
        },
    },

    # Telemedicine 
    'telemedicine': {
        # Select filter example
        'example': {
            'filter_id': 'telemedicine',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'telemedicine',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Bank Account
    'bank-account': {
        # Select filter example
        'example': {
            'filter_id': 'bank-account',
            'selected_values': [
                '0',  # I have my own account
                '1',  # I have a joint account with someone else
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'bank-account',
            'selected_values': [
                '0',  # I have my own account
                '1',  # I have a joint account with someone else
            ],
            'weightings': {
                '0': 1,  # Equal weighting for I have my own account
                '1': 1,  # Equal weighting for I have a joint account with someone else
            }
        },
    },

    # Healthcare provider consultation
    'healthcare-provider-consultation': {
        # Select filter example
        'example': {
            'filter_id': 'healthcare-provider-consultation',
            'selected_values': [
                '0',  # Within the past year
                '1',  # 1 - 2 years ago
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'healthcare-provider-consultation',
            'selected_values': [
                '0',  # Within the past year
                '1',  # 1 - 2 years ago
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Within the past year
                '1': 1,  # Equal weighting for 1 - 2 years ago
            }
        },
    },

    # Touch typing
    'touch-typing': {
        # Select filter example
        'example': {
            'filter_id': 'touch-typing',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'touch-typing',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Dyslexia
    'dyslexia': {
        # Select filter example
        'example': {
            'filter_id': 'dyslexia',
            'selected_values': [
                '0',  # Yes, I have been medically diagnosed with dyslexia
                '1',  # No, but I am in the process of being diagnosed
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'dyslexia',
            'selected_values': [
                '0',  # Yes, I have been medically diagnosed with dyslexia
                '1',  # No, but I am in the process of being diagnosed
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes, I have been medically diagnosed with dyslexia
                '1': 1,  # Equal weighting for No, but I am in the process of being diagnosed
            }
        },
    },

    # Retirement Status
    'retirement-status': {
        # Select filter example
        'example': {
            'filter_id': 'retirement-status',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'retirement-status',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Car Model Year
    'car-model-year': {
        # Select filter example
        'example': {
            'filter_id': 'car-model-year',
            'selected_values': [
                '0',  # 2023
                '1',  # 2022
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'car-model-year',
            'selected_values': [
                '0',  # 2023
                '1',  # 2022
            ],
            'weightings': {
                '0': 1,  # Equal weighting for 2023
                '1': 1,  # Equal weighting for 2022
            }
        },
    },

    # Driving Frequency
    'driving-frequency': {
        # Select filter example
        'example': {
            'filter_id': 'driving-frequency',
            'selected_values': [
                '0',  # Less than an hour
                '1',  # 1 - 7 hours
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'driving-frequency',
            'selected_values': [
                '0',  # Less than an hour
                '1',  # 1 - 7 hours
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Less than an hour
                '1': 1,  # Equal weighting for 1 - 7 hours
            }
        },
    },

    # UK Postcode area
    'uk-postcode-area': {
        # Select filter example
        'example': {
            'filter_id': 'uk-postcode-area',
            'selected_values': [
                '0',  # AB
                '1',  # AL
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'uk-postcode-area',
            'selected_values': [
                '0',  # AB
                '1',  # AL
            ],
            'weightings': {
                '0': 1,  # Equal weighting for AB
                '1': 1,  # Equal weighting for AL
            }
        },
    },

    # Annual Business Turnover
    'annual-business-turnover': {
        # Select filter example
        'example': {
            'filter_id': 'annual-business-turnover',
            'selected_values': [
                '0',  # Less than £100k
                '1',  # £100k - £500k
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'annual-business-turnover',
            'selected_values': [
                '0',  # Less than £100k
                '1',  # £100k - £500k
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Less than £100k
                '1': 1,  # Equal weighting for £100k - £500k
            }
        },
    },

    # Future Car Ownership
    'future-car-ownership': {
        # Select filter example
        'example': {
            'filter_id': 'future-car-ownership',
            'selected_values': [
                '0',  # I will own a car in the future
                '1',  # I am likely to own a car in the future
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'future-car-ownership',
            'selected_values': [
                '0',  # I will own a car in the future
                '1',  # I am likely to own a car in the future
            ],
            'weightings': {
                '0': 1,  # Equal weighting for I will own a car in the future
                '1': 1,  # Equal weighting for I am likely to own a car in the future
            }
        },
    },

    # Pension Income
    'pension-income': {
        # Select filter example
        'example': {
            'filter_id': 'pension-income',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'pension-income',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Pension Plan
    'pension-plan': {
        # Select filter example
        'example': {
            'filter_id': 'pension-plan',
            'selected_values': [
                '0',  # I have a workplace pension
                '1',  # I have a self-arranged private pension
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'pension-plan',
            'selected_values': [
                '0',  # I have a workplace pension
                '1',  # I have a self-arranged private pension
            ],
            'weightings': {
                '0': 1,  # Equal weighting for I have a workplace pension
                '1': 1,  # Equal weighting for I have a self-arranged private pension
            }
        },
    },

    # Harmful Content
    'harmful-content': {
        # Select filter example
        'example': {
            'filter_id': 'harmful-content',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'harmful-content',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Years of Management Experience
    'years-of-management-experience': {
        # Select filter example
        'example': {
            'filter_id': 'years-of-management-experience',
            'selected_values': [
                '0',  # I've never managed a subordinate
                '1',  # Less than 1 year
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'years-of-management-experience',
            'selected_values': [
                '0',  # I've never managed a subordinate
                '1',  # Less than 1 year
            ],
            'weightings': {
                '0': 1,  # Equal weighting for I've never managed a subordinate
                '1': 1,  # Equal weighting for Less than 1 year
            }
        },
    },

    # Anxiety Severity
    'anxiety-severity': {
        # Select filter example
        'example': {
            'filter_id': 'anxiety-severity',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'anxiety-severity',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Mental Health Diagnosis
    'mental-health-diagnosis': {
        # Select filter example
        'example': {
            'filter_id': 'mental-health-diagnosis',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'mental-health-diagnosis',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Prescription Medications
    'prescription-medications': {
        # Select filter example
        'example': {
            'filter_id': 'prescription-medications',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'prescription-medications',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Illustration Experience
    'illustration-experience': {
        # Select filter example
        'example': {
            'filter_id': 'illustration-experience',
            'selected_values': [
                '0',  # Yes, I am a professional illustrator
                '1',  # Yes, I have some experience creating illustrations as part of my work
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'illustration-experience',
            'selected_values': [
                '0',  # Yes, I am a professional illustrator
                '1',  # Yes, I have some experience creating illustrations as part of my work
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes, I am a professional illustrator
                '1': 1,  # Equal weighting for Yes, I have some experience creating illustrations as part of my work
            }
        },
    },

    # Degree subject
    'degree-subject': {
        # Select filter example
        'example': {
            'filter_id': 'degree-subject',
            'selected_values': [
                '0',  # Arts & Humanities
                '1',  # Education
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'degree-subject',
            'selected_values': [
                '0',  # Arts & Humanities
                '1',  # Education
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Arts & Humanities
                '1': 1,  # Equal weighting for Education
            }
        },
    },

    # Employment role
    'employment-role': {
        # Select filter example
        'example': {
            'filter_id': 'employment-role',
            'selected_values': [
                '0',  # Teacher
                '1',  # Journalist
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'employment-role',
            'selected_values': [
                '0',  # Teacher
                '1',  # Journalist
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Teacher
                '1': 1,  # Equal weighting for Journalist
            }
        },
    },

    # Active interests
    'active-interests': {
        # Select filter example
        'example': {
            'filter_id': 'active-interests',
            'selected_values': [
                '0',  # Influencer
                '1',  # Blogger
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'active-interests',
            'selected_values': [
                '0',  # Influencer
                '1',  # Blogger
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Influencer
                '1': 1,  # Equal weighting for Blogger
            }
        },
    },

    # Financial decision-making
    'financial-decision-making': {
        # Select filter example
        'example': {
            'filter_id': 'financial-decision-making',
            'selected_values': [
                '0',  # I am the primary financial decision-maker
                '1',  # I share equally in financial decisions
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'financial-decision-making',
            'selected_values': [
                '0',  # I am the primary financial decision-maker
                '1',  # I share equally in financial decisions
            ],
            'weightings': {
                '0': 1,  # Equal weighting for I am the primary financial decision-maker
                '1': 1,  # Equal weighting for I share equally in financial decisions
            }
        },
    },

    # Car ownership
    'car-ownership': {
        # Select filter example
        'example': {
            'filter_id': 'car-ownership',
            'selected_values': [
                '0',  # I own a car
                '1',  # I lease a car
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'car-ownership',
            'selected_values': [
                '0',  # I own a car
                '1',  # I lease a car
            ],
            'weightings': {
                '0': 1,  # Equal weighting for I own a car
                '1': 1,  # Equal weighting for I lease a car
            }
        },
    },

    # Current car type
    'current-car-type': {
        # Select filter example
        'example': {
            'filter_id': 'current-car-type',
            'selected_values': [
                '0',  # Petrol
                '1',  # Diesel
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'current-car-type',
            'selected_values': [
                '0',  # Petrol
                '1',  # Diesel
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Petrol
                '1': 1,  # Equal weighting for Diesel
            }
        },
    },

    # Eligible voter (UK)
    'eligible-voter-uk': {
        # Select filter example
        'example': {
            'filter_id': 'eligible-voter-uk',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'eligible-voter-uk',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Dentistry
    'dentistry': {
        # Select filter example
        'example': {
            'filter_id': 'dentistry',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'dentistry',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Work Function
    'work-function': {
        # Select filter example
        'example': {
            'filter_id': 'work-function',
            'selected_values': [
                '0',  # Account Management
                '1',  # Administration/ Personal Assistant
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'work-function',
            'selected_values': [
                '0',  # Account Management
                '1',  # Administration/ Personal Assistant
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Account Management
                '1': 1,  # Equal weighting for Administration/ Personal Assistant
            }
        },
    },

    # Work Role
    'work-role': {
        # Select filter example
        'example': {
            'filter_id': 'work-role',
            'selected_values': [
                '0',  # CEO or C-suite Executive
                '1',  # President
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'work-role',
            'selected_values': [
                '0',  # CEO or C-suite Executive
                '1',  # President
            ],
            'weightings': {
                '0': 1,  # Equal weighting for CEO or C-suite Executive
                '1': 1,  # Equal weighting for President
            }
        },
    },

    # Method of work
    'method-of-work': {
        # Select filter example
        'example': {
            'filter_id': 'method-of-work',
            'selected_values': [
                '0',  # I use a computer or mobile device for 75% or more of my work
                '1',  # I use a computer or mobile device for 50% to 74% of my work
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'method-of-work',
            'selected_values': [
                '0',  # I use a computer or mobile device for 75% or more of my work
                '1',  # I use a computer or mobile device for 50% to 74% of my work
            ],
            'weightings': {
                '0': 1,  # Equal weighting for I use a computer or mobile device for 75% or more of my work
                '1': 1,  # Equal weighting for I use a computer or mobile device for 50% to 74% of my work
            }
        },
    },

    # Weekly Ai (Artificial Intelligence) use
    'weekly-ai-artificial-intelligence-use': {
        # Select filter example
        'example': {
            'filter_id': 'weekly-ai-artificial-intelligence-use',
            'selected_values': [
                '0',  # Never
                '1',  # Once a Week
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'weekly-ai-artificial-intelligence-use',
            'selected_values': [
                '0',  # Never
                '1',  # Once a Week
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Never
                '1': 1,  # Equal weighting for Once a Week
            }
        },
    },

    # Voter Registration (US)
    'voter-registration-us': {
        # Select filter example
        'example': {
            'filter_id': 'voter-registration-us',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'voter-registration-us',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # UK Main Bank Account
    'uk-main-bank-account': {
        # Select filter example
        'example': {
            'filter_id': 'uk-main-bank-account',
            'selected_values': [
                '0',  # Barclays
                '1',  # Bank of Scotland
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'uk-main-bank-account',
            'selected_values': [
                '0',  # Barclays
                '1',  # Bank of Scotland
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Barclays
                '1': 1,  # Equal weighting for Bank of Scotland
            }
        },
    },

    # Years of Work Experience
    'years-of-work-experience': {
        # Select filter example
        'example': {
            'filter_id': 'years-of-work-experience',
            'selected_values': [
                '0',  # Less than one year
                '1',  # 1-2 years
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'years-of-work-experience',
            'selected_values': [
                '0',  # Less than one year
                '1',  # 1-2 years
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Less than one year
                '1': 1,  # Equal weighting for 1-2 years
            }
        },
    },

    # UK Parliamentary Constituency
    'uk-parliamentary-constituency': {
        # Select filter example
        'example': {
            'filter_id': 'uk-parliamentary-constituency',
            'selected_values': [
                '0',  # Aberavon
                '1',  # Aberconwy
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'uk-parliamentary-constituency',
            'selected_values': [
                '0',  # Aberavon
                '1',  # Aberconwy
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Aberavon
                '1': 1,  # Equal weighting for Aberconwy
            }
        },
    },

    # Ozempic
    'ozempic': {
        # Select filter example
        'example': {
            'filter_id': 'ozempic',
            'selected_values': [
                '0',  # Yes, I am currently taking Ozempic
                '1',  # No, I am not currently taking Ozempic but I have in the past
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'ozempic',
            'selected_values': [
                '0',  # Yes, I am currently taking Ozempic
                '1',  # No, I am not currently taking Ozempic but I have in the past
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes, I am currently taking Ozempic
                '1': 1,  # Equal weighting for No, I am not currently taking Ozempic but I have in the past
            }
        },
    },

    # Current investable assets (GBP)
    'current-investable-assets-gbp': {
        # Select filter example
        'example': {
            'filter_id': 'current-investable-assets-gbp',
            'selected_values': [
                '0',  # Less than £1,500
                '1',  # £1,500 - £7,499
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'current-investable-assets-gbp',
            'selected_values': [
                '0',  # Less than £1,500
                '1',  # £1,500 - £7,499
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Less than £1,500
                '1': 1,  # Equal weighting for £1,500 - £7,499
            }
        },
    },

    # Current investable assets (USD) [US participants only]
    'current-investable-assets-usd': {
        # Select filter example
        'example': {
            'filter_id': 'current-investable-assets-usd',
            'selected_values': [
                '0',  # Less than $1,500
                '1',  # $1,500 - $7,499
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'current-investable-assets-usd',
            'selected_values': [
                '0',  # Less than $1,500
                '1',  # $1,500 - $7,499
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Less than $1,500
                '1': 1,  # Equal weighting for $1,500 - $7,499
            }
        },
    },

    # Current Canadian province of residence
    'current-canadian-province-of-residence': {
        # Select filter example
        'example': {
            'filter_id': 'current-canadian-province-of-residence',
            'selected_values': [
                '0',  # Newfoundland and Labrador
                '1',  # Prince Edward Island
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'current-canadian-province-of-residence',
            'selected_values': [
                '0',  # Newfoundland and Labrador
                '1',  # Prince Edward Island
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Newfoundland and Labrador
                '1': 1,  # Equal weighting for Prince Edward Island
            }
        },
    },

    # New York Times Users
    'new-york-times-users': {
        # Select filter example
        'example': {
            'filter_id': 'new-york-times-users',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'new-york-times-users',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Annual Business Turnover (US)
    'annual-business-turnover-us': {
        # Select filter example
        'example': {
            'filter_id': 'annual-business-turnover-us',
            'selected_values': [
                '0',  # Less than $100k
                '1',  # $100k - $500k
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'annual-business-turnover-us',
            'selected_values': [
                '0',  # Less than $100k
                '1',  # $100k - $500k
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Less than $100k
                '1': 1,  # Equal weighting for $100k - $500k
            }
        },
    },

    # Employment Role within Information Technology
    'employment-role-within-information-technology': {
        # Select filter example
        'example': {
            'filter_id': 'employment-role-within-information-technology',
            'selected_values': [
                '0',  # Service Management
                '1',  # Operations Management
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'employment-role-within-information-technology',
            'selected_values': [
                '0',  # Service Management
                '1',  # Operations Management
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Service Management
                '1': 1,  # Equal weighting for Operations Management
            }
        },
    },

    # Weekly working hours on Prolific
    'weekly-working-hours-on-prolific': {
        # Select filter example
        'example': {
            'filter_id': 'weekly-working-hours-on-prolific',
            'selected_values': [
                '0',  # 0 - 5 hours
                '1',  # 6 - 10 hours
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'weekly-working-hours-on-prolific',
            'selected_values': [
                '0',  # 0 - 5 hours
                '1',  # 6 - 10 hours
            ],
            'weightings': {
                '0': 1,  # Equal weighting for 0 - 5 hours
                '1': 1,  # Equal weighting for 6 - 10 hours
            }
        },
    },

    # Weight Loss Products
    'weight-loss-products': {
        # Select filter example
        'example': {
            'filter_id': 'weight-loss-products',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'weight-loss-products',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Weight Loss
    'weight-loss': {
        # Select filter example
        'example': {
            'filter_id': 'weight-loss',
            'selected_values': [
                '0',  # Yes, I am currently on a diet
                '1',  # No, but I am considering it in the future
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'weight-loss',
            'selected_values': [
                '0',  # Yes, I am currently on a diet
                '1',  # No, but I am considering it in the future
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes, I am currently on a diet
                '1': 1,  # Equal weighting for No, but I am considering it in the future
            }
        },
    },

    # Personal Income (Euro)
    'personal-income-euro': {
        # Select filter example
        'example': {
            'filter_id': 'personal-income-euro',
            'selected_values': [
                '0',  # Less than €10,000
                '1',  # €10,000 - €19,999
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'personal-income-euro',
            'selected_values': [
                '0',  # Less than €10,000
                '1',  # €10,000 - €19,999
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Less than €10,000
                '1': 1,  # Equal weighting for €10,000 - €19,999
            }
        },
    },

    # Household Income (Euro)
    'household-income-euro': {
        # Select filter example
        'example': {
            'filter_id': 'household-income-euro',
            'selected_values': [
                '0',  # Less than €10,000
                '1',  # €10,000 - €19,999
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'household-income-euro',
            'selected_values': [
                '0',  # Less than €10,000
                '1',  # €10,000 - €19,999
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Less than €10,000
                '1': 1,  # Equal weighting for €10,000 - €19,999
            }
        },
    },

    # Personal Income (USD) [US participants only]
    'personal-income-usd-us-participants-only': {
        # Select filter example
        'example': {
            'filter_id': 'personal-income-usd-us-participants-only',
            'selected_values': [
                '0',  # Less than $10,000
                '1',  # $10,000 - $19,999
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'personal-income-usd-us-participants-only',
            'selected_values': [
                '0',  # Less than $10,000
                '1',  # $10,000 - $19,999
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Less than $10,000
                '1': 1,  # Equal weighting for $10,000 - $19,999
            }
        },
    },

    # Personal Income (Dollars) [Non US participants only]
    'personal-income-dollars-non-us-participants-only': {
        # Select filter example
        'example': {
            'filter_id': 'personal-income-dollars-non-us-participants-only',
            'selected_values': [
                '0',  # Less than $10,000
                '1',  # $10,000 - $19,999
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'personal-income-dollars-non-us-participants-only',
            'selected_values': [
                '0',  # Less than $10,000
                '1',  # $10,000 - $19,999
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Less than $10,000
                '1': 1,  # Equal weighting for $10,000 - $19,999
            }
        },
    },

    # Grades taught - Primary/Secondary (K-12)
    'grades-taught-primarysecondary-k-12': {
        # Select filter example
        'example': {
            'filter_id': 'grades-taught-primarysecondary-k-12',
            'selected_values': [
                '0',  # Kindergarten
                '1',  # 1st grade
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'grades-taught-primarysecondary-k-12',
            'selected_values': [
                '0',  # Kindergarten
                '1',  # 1st grade
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Kindergarten
                '1': 1,  # Equal weighting for 1st grade
            }
        },
    },

    # Online Banking
    'online-banking': {
        # Select filter example
        'example': {
            'filter_id': 'online-banking',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'online-banking',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Credit Card 
    'credit-card': {
        # Select filter example
        'example': {
            'filter_id': 'credit-card',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'credit-card',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Current investable assets (Dollars) [Non US participants only]
    'current-investable-assets-dollars-non-us-participants-only': {
        # Select filter example
        'example': {
            'filter_id': 'current-investable-assets-dollars-non-us-participants-only',
            'selected_values': [
                '0',  # Less than $1,500
                '1',  # $1,500 - $7,499
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'current-investable-assets-dollars-non-us-participants-only',
            'selected_values': [
                '0',  # Less than $1,500
                '1',  # $1,500 - $7,499
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Less than $1,500
                '1': 1,  # Equal weighting for $1,500 - $7,499
            }
        },
    },

    # Press Releases
    'press-releases': {
        # Select filter example
        'example': {
            'filter_id': 'press-releases',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'press-releases',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # App Download 
    'app-download': {
        # Select filter example
        'example': {
            'filter_id': 'app-download',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'app-download',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Remote Degree Programs
    'remote-degree-programs': {
        # Select filter example
        'example': {
            'filter_id': 'remote-degree-programs',
            'selected_values': [
                '0',  # Yes, currently following a Remote Degree Program
                '1',  # No, I am not following a Remote Degree Program
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'remote-degree-programs',
            'selected_values': [
                '0',  # Yes, currently following a Remote Degree Program
                '1',  # No, I am not following a Remote Degree Program
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes, currently following a Remote Degree Program
                '1': 1,  # Equal weighting for No, I am not following a Remote Degree Program
            }
        },
    },

    # AI tasker characteristics
    'ai-tasker-characteristics': {
        # Select filter example
        'example': {
            'filter_id': 'ai-tasker-characteristics',
            'selected_values': [
                '0',  # Never
                '1',  # Rarely (Yearly)
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'ai-tasker-characteristics',
            'selected_values': [
                '0',  # Never
                '1',  # Rarely (Yearly)
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Never
                '1': 1,  # Equal weighting for Rarely (Yearly)
            }
        },
    },

    # Prior Participation in AI Research Studies
    'prior-participation-in-ai-research-studies': {
        # Select filter example
        'example': {
            'filter_id': 'prior-participation-in-ai-research-studies',
            'selected_values': [
                '0',  # None
                '1',  # 1-10
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'prior-participation-in-ai-research-studies',
            'selected_values': [
                '0',  # None
                '1',  # 1-10
            ],
            'weightings': {
                '0': 1,  # Equal weighting for None
                '1': 1,  # Equal weighting for 1-10
            }
        },
    },

    # UK General Election 2024	
    'uk-general-election-2024': {
        # Select filter example
        'example': {
            'filter_id': 'uk-general-election-2024',
            'selected_values': [
                '0',  # Conservatives
                '1',  # Labour
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'uk-general-election-2024',
            'selected_values': [
                '0',  # Conservatives
                '1',  # Labour
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Conservatives
                '1': 1,  # Equal weighting for Labour
            }
        },
    },

    # Disposable income (GBP)
    'disposable-income-gbp': {
        # Select filter example
        'example': {
            'filter_id': 'disposable-income-gbp',
            'selected_values': [
                '0',  # Less than £50
                '1',  # £51-£100
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'disposable-income-gbp',
            'selected_values': [
                '0',  # Less than £50
                '1',  # £51-£100
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Less than £50
                '1': 1,  # Equal weighting for £51-£100
            }
        },
    },

    # Attitudes towards Financial Risk 
    'attitudes-towards-financial-risk': {
        # Select filter example
        'example': {
            'filter_id': 'attitudes-towards-financial-risk',
            'selected_values': [
                '0',  # I try to avoid financial risks – I prefer certainty
                '1',  # I am cautious and prefer low-risk investments
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'attitudes-towards-financial-risk',
            'selected_values': [
                '0',  # I try to avoid financial risks – I prefer certainty
                '1',  # I am cautious and prefer low-risk investments
            ],
            'weightings': {
                '0': 1,  # Equal weighting for I try to avoid financial risks – I prefer certainty
                '1': 1,  # Equal weighting for I am cautious and prefer low-risk investments
            }
        },
    },

    # Total Value of Invested Assets (Excluding Property)
    'total-value-of-invested-assets-excluding-property': {
        # Select filter example
        'example': {
            'filter_id': 'total-value-of-invested-assets-excluding-property',
            'selected_values': [
                '0',  # I do not currently have any invested assets
                '1',  # Less than £10,000
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'total-value-of-invested-assets-excluding-property',
            'selected_values': [
                '0',  # I do not currently have any invested assets
                '1',  # Less than £10,000
            ],
            'weightings': {
                '0': 1,  # Equal weighting for I do not currently have any invested assets
                '1': 1,  # Equal weighting for Less than £10,000
            }
        },
    },

    # How many hours of sport do you watch
    'how-many-hours-of-sport-do-you-watch': {
        # Select filter example
        'example': {
            'filter_id': 'how-many-hours-of-sport-do-you-watch',
            'selected_values': [
                '0',  # 0-2
                '1',  # 2-4
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'how-many-hours-of-sport-do-you-watch',
            'selected_values': [
                '0',  # 0-2
                '1',  # 2-4
            ],
            'weightings': {
                '0': 1,  # Equal weighting for 0-2
                '1': 1,  # Equal weighting for 2-4
            }
        },
    },

    # Cars in the company fleet
    'cars-in-the-company-fleet': {
        # Select filter example
        'example': {
            'filter_id': 'cars-in-the-company-fleet',
            'selected_values': [
                '0',  # 0 – 5
                '1',  # 6 – 10
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'cars-in-the-company-fleet',
            'selected_values': [
                '0',  # 0 – 5
                '1',  # 6 – 10
            ],
            'weightings': {
                '0': 1,  # Equal weighting for 0 – 5
                '1': 1,  # Equal weighting for 6 – 10
            }
        },
    },

    # International Students
    'international-students': {
        # Select filter example
        'example': {
            'filter_id': 'international-students',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'international-students',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # AI taskers
    'ai-taskers': {
        # Select filter example
        'example': {
            'filter_id': 'ai-taskers',
            'selected_values': [
                '0',  # Qualified AI taskers
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'ai-taskers',
            'selected_values': [
                '0',  # Qualified AI taskers
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Qualified AI taskers
            }
        },
    },

    # 2024 US presidential election
    '2024-us-presidential-election': {
        # Select filter example
        'example': {
            'filter_id': '2024-us-presidential-election',
            'selected_values': [
                '0',  # Kamala Harris
                '1',  # Donald Trump
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': '2024-us-presidential-election',
            'selected_values': [
                '0',  # Kamala Harris
                '1',  # Donald Trump
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Kamala Harris
                '1': 1,  # Equal weighting for Donald Trump
            }
        },
    },

    # Standard Employees
    'standard-employees': {
        # Select filter example
        'example': {
            'filter_id': 'standard-employees',
            'selected_values': [
                '0',  # 1
                '1',  # 2-10
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'standard-employees',
            'selected_values': [
                '0',  # 1
                '1',  # 2-10
            ],
            'weightings': {
                '0': 1,  # Equal weighting for 1
                '1': 1,  # Equal weighting for 2-10
            }
        },
    },

    # Organization Type
    'organization-type': {
        # Select filter example
        'example': {
            'filter_id': 'organization-type',
            'selected_values': [
                '0',  # A for-profit, business-to-business company (B2B)
                '1',  # A for-profit, business-to-consumer company (B2C)
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'organization-type',
            'selected_values': [
                '0',  # A for-profit, business-to-business company (B2B)
                '1',  # A for-profit, business-to-consumer company (B2C)
            ],
            'weightings': {
                '0': 1,  # Equal weighting for A for-profit, business-to-business company (B2B)
                '1': 1,  # Equal weighting for A for-profit, business-to-consumer company (B2C)
            }
        },
    },

    # Job Position 
    'job-position': {
        # Select filter example
        'example': {
            'filter_id': 'job-position',
            'selected_values': [
                '0',  # C-Level (e.g. CEO, CFO), Owner, Partner, President
                '1',  # Vice President (EVP, SVP, AVP, VP)
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'job-position',
            'selected_values': [
                '0',  # C-Level (e.g. CEO, CFO), Owner, Partner, President
                '1',  # Vice President (EVP, SVP, AVP, VP)
            ],
            'weightings': {
                '0': 1,  # Equal weighting for C-Level (e.g. CEO, CFO), Owner, Partner, President
                '1': 1,  # Equal weighting for Vice President (EVP, SVP, AVP, VP)
            }
        },
    },

    # Arabic
    'arabic': {
        # Select filter example
        'example': {
            'filter_id': 'arabic',
            'selected_values': [
                '0',  # Arabic
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'arabic',
            'selected_values': [
                '0',  # Arabic
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Arabic
            }
        },
    },

    # Cantonese
    'cantonese': {
        # Select filter example
        'example': {
            'filter_id': 'cantonese',
            'selected_values': [
                '0',  # Cantonese
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'cantonese',
            'selected_values': [
                '0',  # Cantonese
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Cantonese
            }
        },
    },

    # Dutch
    'dutch': {
        # Select filter example
        'example': {
            'filter_id': 'dutch',
            'selected_values': [
                '0',  # Dutch
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'dutch',
            'selected_values': [
                '0',  # Dutch
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Dutch
            }
        },
    },

    # French
    'french': {
        # Select filter example
        'example': {
            'filter_id': 'french',
            'selected_values': [
                '0',  # French
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'french',
            'selected_values': [
                '0',  # French
            ],
            'weightings': {
                '0': 1,  # Equal weighting for French
            }
        },
    },

    # German
    'german': {
        # Select filter example
        'example': {
            'filter_id': 'german',
            'selected_values': [
                '0',  # German
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'german',
            'selected_values': [
                '0',  # German
            ],
            'weightings': {
                '0': 1,  # Equal weighting for German
            }
        },
    },

    # Italian
    'italian': {
        # Select filter example
        'example': {
            'filter_id': 'italian',
            'selected_values': [
                '0',  # Italian
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'italian',
            'selected_values': [
                '0',  # Italian
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Italian
            }
        },
    },

    # Japanese
    'japanese': {
        # Select filter example
        'example': {
            'filter_id': 'japanese',
            'selected_values': [
                '0',  # Japanese
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'japanese',
            'selected_values': [
                '0',  # Japanese
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Japanese
            }
        },
    },

    # Korean
    'korean': {
        # Select filter example
        'example': {
            'filter_id': 'korean',
            'selected_values': [
                '0',  # Korean
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'korean',
            'selected_values': [
                '0',  # Korean
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Korean
            }
        },
    },

    # Mandarin
    'mandarin': {
        # Select filter example
        'example': {
            'filter_id': 'mandarin',
            'selected_values': [
                '0',  # Mandarin
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'mandarin',
            'selected_values': [
                '0',  # Mandarin
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Mandarin
            }
        },
    },

    # Portuguese
    'portuguese': {
        # Select filter example
        'example': {
            'filter_id': 'portuguese',
            'selected_values': [
                '0',  # Portuguese
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'portuguese',
            'selected_values': [
                '0',  # Portuguese
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Portuguese
            }
        },
    },

    # Spanish
    'spanish': {
        # Select filter example
        'example': {
            'filter_id': 'spanish',
            'selected_values': [
                '0',  # Spanish
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'spanish',
            'selected_values': [
                '0',  # Spanish
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Spanish
            }
        },
    },

    # Java
    'java': {
        # Select filter example
        'example': {
            'filter_id': 'java',
            'selected_values': [
                '0',  # Java
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'java',
            'selected_values': [
                '0',  # Java
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Java
            }
        },
    },

    # Javascript
    'javascript': {
        # Select filter example
        'example': {
            'filter_id': 'javascript',
            'selected_values': [
                '0',  # Javascript
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'javascript',
            'selected_values': [
                '0',  # Javascript
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Javascript
            }
        },
    },

    # SQL
    'sql': {
        # Select filter example
        'example': {
            'filter_id': 'sql',
            'selected_values': [
                '0',  # SQL
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'sql',
            'selected_values': [
                '0',  # SQL
            ],
            'weightings': {
                '0': 1,  # Equal weighting for SQL
            }
        },
    },

    # Python
    'python': {
        # Select filter example
        'example': {
            'filter_id': 'python',
            'selected_values': [
                '0',  # Python
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'python',
            'selected_values': [
                '0',  # Python
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Python
            }
        },
    },

    # Mathematics
    'mathematics': {
        # Select filter example
        'example': {
            'filter_id': 'mathematics',
            'selected_values': [
                '0',  # Mathematics
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'mathematics',
            'selected_values': [
                '0',  # Mathematics
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Mathematics
            }
        },
    },

    # General Practitioners
    'general-practitioners': {
        # Select filter example
        'example': {
            'filter_id': 'general-practitioners',
            'selected_values': [
                '0',  # General Practitioners
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'general-practitioners',
            'selected_values': [
                '0',  # General Practitioners
            ],
            'weightings': {
                '0': 1,  # Equal weighting for General Practitioners
            }
        },
    },

    # Free From Products
    'free-from-products': {
        # Select filter example
        'example': {
            'filter_id': 'free-from-products',
            'selected_values': [
                '0',  # Soya milk
                '1',  # Almond milk
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'free-from-products',
            'selected_values': [
                '0',  # Soya milk
                '1',  # Almond milk
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Soya milk
                '1': 1,  # Equal weighting for Almond milk
            }
        },
    },

    # Health Insurance (US)
    'health-insurance-us': {
        # Select filter example
        'example': {
            'filter_id': 'health-insurance-us',
            'selected_values': [
                '0',  # Medicaid and\or Medicare
                '1',  # Private or Employment based health insurance
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'health-insurance-us',
            'selected_values': [
                '0',  # Medicaid and\or Medicare
                '1',  # Private or Employment based health insurance
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Medicaid and\or Medicare
                '1': 1,  # Equal weighting for Private or Employment based health insurance
            }
        },
    },

    # Long-term health condition or disability
    'long-term-health-condition-or-disability': {
        # Select filter example
        'example': {
            'filter_id': 'long-term-health-condition-or-disability',
            'selected_values': [
                '0',  # Vision impairment
                '1',  # Hearing impairment
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'long-term-health-condition-or-disability',
            'selected_values': [
                '0',  # Vision impairment
                '1',  # Hearing impairment
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Vision impairment
                '1': 1,  # Equal weighting for Hearing impairment
            }
        },
    },

    # Game types
    'game-types': {
        # Select filter example
        'example': {
            'filter_id': 'game-types',
            'selected_values': [
                '0',  # Computer games
                '1',  # Console games
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'game-types',
            'selected_values': [
                '0',  # Computer games
                '1',  # Console games
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Computer games
                '1': 1,  # Equal weighting for Console games
            }
        },
    },

    # Simulated Experiences
    'simulated-experiences': {
        # Select filter example
        'example': {
            'filter_id': 'simulated-experiences',
            'selected_values': [
                '0',  # Virtual reality
                '1',  # Augmented reality
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'simulated-experiences',
            'selected_values': [
                '0',  # Virtual reality
                '1',  # Augmented reality
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Virtual reality
                '1': 1,  # Equal weighting for Augmented reality
            }
        },
    },

    # Subject
    'subject': {
        # Select filter example
        'example': {
            'filter_id': 'subject',
            'selected_values': [
                '0',  # Accounting
                '1',  # Agriculture and Horticulture
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'subject',
            'selected_values': [
                '0',  # Accounting
                '1',  # Agriculture and Horticulture
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Accounting
                '1': 1,  # Equal weighting for Agriculture and Horticulture
            }
        },
    },

    # Gender identity non-binary only
    'gender-identity-non-binary-only': {
        # Select filter example
        'example': {
            'filter_id': 'gender-identity-non-binary-only',
            'selected_values': [
                '0',  # Man (including Trans Male/Trans Man)
                '1',  # Woman (including Trans Female/Trans Woman)
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'gender-identity-non-binary-only',
            'selected_values': [
                '0',  # Man (including Trans Male/Trans Man)
                '1',  # Woman (including Trans Female/Trans Woman)
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Man (including Trans Male/Trans Man)
                '1': 1,  # Equal weighting for Woman (including Trans Female/Trans Woman)
            }
        },
    },

    # Diet Restriction
    'diet-restriction': {
        # Select filter example
        'example': {
            'filter_id': 'diet-restriction',
            'selected_values': [
                '0',  # Vegetarian
                '1',  # Vegan
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'diet-restriction',
            'selected_values': [
                '0',  # Vegetarian
                '1',  # Vegan
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Vegetarian
                '1': 1,  # Equal weighting for Vegan
            }
        },
    },

    # Car Brand
    'car-brand': {
        # Select filter example
        'example': {
            'filter_id': 'car-brand',
            'selected_values': [
                '0',  # Alfa Romeo
                '1',  # Audi
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'car-brand',
            'selected_values': [
                '0',  # Alfa Romeo
                '1',  # Audi
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Alfa Romeo
                '1': 1,  # Equal weighting for Audi
            }
        },
    },

    # Music Streaming Services
    'music-streaming-services': {
        # Select filter example
        'example': {
            'filter_id': 'music-streaming-services',
            'selected_values': [
                '0',  # Spotify
                '1',  # Apple Music
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'music-streaming-services',
            'selected_values': [
                '0',  # Spotify
                '1',  # Apple Music
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Spotify
                '1': 1,  # Equal weighting for Apple Music
            }
        },
    },

    # Gender Identity of Romantic Partners
    'gender-identity-of-romantic-partners': {
        # Select filter example
        'example': {
            'filter_id': 'gender-identity-of-romantic-partners',
            'selected_values': [
                '0',  # I have a current partner, who is a man (including trans men)
                '1',  # I have a current partner, who is a woman (including trans women)
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'gender-identity-of-romantic-partners',
            'selected_values': [
                '0',  # I have a current partner, who is a man (including trans men)
                '1',  # I have a current partner, who is a woman (including trans women)
            ],
            'weightings': {
                '0': 1,  # Equal weighting for I have a current partner, who is a man (including trans men)
                '1': 1,  # Equal weighting for I have a current partner, who is a woman (including trans women)
            }
        },
    },

    # Household electric vehicle ownership or leasing
    'household-electric-vehicle-ownership-or-leasing': {
        # Select filter example
        'example': {
            'filter_id': 'household-electric-vehicle-ownership-or-leasing',
            'selected_values': [
                '0',  # Yes, electric car or van
                '1',  # Yes, electric motorcycle
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'household-electric-vehicle-ownership-or-leasing',
            'selected_values': [
                '0',  # Yes, electric car or van
                '1',  # Yes, electric motorcycle
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes, electric car or van
                '1': 1,  # Equal weighting for Yes, electric motorcycle
            }
        },
    },

    # TV Streaming Services
    'tv-streaming-services': {
        # Select filter example
        'example': {
            'filter_id': 'tv-streaming-services',
            'selected_values': [
                '0',  # Netflix
                '1',  # Amazon Prime Video
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'tv-streaming-services',
            'selected_values': [
                '0',  # Netflix
                '1',  # Amazon Prime Video
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Netflix
                '1': 1,  # Equal weighting for Amazon Prime Video
            }
        },
    },

    # Cryptocurrency Exchanges
    'cryptocurrency-exchanges': {
        # Select filter example
        'example': {
            'filter_id': 'cryptocurrency-exchanges',
            'selected_values': [
                '0',  # Binance
                '1',  # Coinbase
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'cryptocurrency-exchanges',
            'selected_values': [
                '0',  # Binance
                '1',  # Coinbase
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Binance
                '1': 1,  # Equal weighting for Coinbase
            }
        },
    },

    # Food Delivery Services UK
    'food-delivery-services-uk': {
        # Select filter example
        'example': {
            'filter_id': 'food-delivery-services-uk',
            'selected_values': [
                '0',  # Deliveroo
                '1',  # JustEat
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'food-delivery-services-uk',
            'selected_values': [
                '0',  # Deliveroo
                '1',  # JustEat
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Deliveroo
                '1': 1,  # Equal weighting for JustEat
            }
        },
    },

    # Food Delivery Services U.S.
    'food-delivery-services-us': {
        # Select filter example
        'example': {
            'filter_id': 'food-delivery-services-us',
            'selected_values': [
                '0',  # Grubhub
                '1',  # Postmates
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'food-delivery-services-us',
            'selected_values': [
                '0',  # Grubhub
                '1',  # Postmates
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Grubhub
                '1': 1,  # Equal weighting for Postmates
            }
        },
    },

    # Video call interview
    'video-call-interview': {
        # Select filter example
        'example': {
            'filter_id': 'video-call-interview',
            'selected_values': [
                '0',  # Yes, I would be willing to take part in a face to face video interview
                '1',  # Yes, I would be willing to take part in a non-video interview
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'video-call-interview',
            'selected_values': [
                '0',  # Yes, I would be willing to take part in a face to face video interview
                '1',  # Yes, I would be willing to take part in a non-video interview
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes, I would be willing to take part in a face to face video interview
                '1': 1,  # Equal weighting for Yes, I would be willing to take part in a non-video interview
            }
        },
    },

    # Trading Platforms
    'trading-platforms': {
        # Select filter example
        'example': {
            'filter_id': 'trading-platforms',
            'selected_values': [
                '0',  # Acorns
                '1',  # AJ Bell Youinvest
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'trading-platforms',
            'selected_values': [
                '0',  # Acorns
                '1',  # AJ Bell Youinvest
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Acorns
                '1': 1,  # Equal weighting for AJ Bell Youinvest
            }
        },
    },

    # Airlines
    'airlines': {
        # Select filter example
        'example': {
            'filter_id': 'airlines',
            'selected_values': [
                '0',  # Aegean Airlines
                '1',  # Aer Lingus
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'airlines',
            'selected_values': [
                '0',  # Aegean Airlines
                '1',  # Aer Lingus
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Aegean Airlines
                '1': 1,  # Equal weighting for Aer Lingus
            }
        },
    },

    # Camera usage
    'camera-usage': {
        # Select filter example
        'example': {
            'filter_id': 'camera-usage',
            'selected_values': [
                '0',  # Action
                '1',  # DSLR
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'camera-usage',
            'selected_values': [
                '0',  # Action
                '1',  # DSLR
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Action
                '1': 1,  # Equal weighting for DSLR
            }
        },
    },

    # Primary Language
    'primary-language': {
        # Select filter example
        'example': {
            'filter_id': 'primary-language',
            'selected_values': [
                '0',  # Afrikaans
                '1',  # Albanian
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'primary-language',
            'selected_values': [
                '0',  # Afrikaans
                '1',  # Albanian
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Afrikaans
                '1': 1,  # Equal weighting for Albanian
            }
        },
    },

    # Earliest Language in Life
    'earliest-language-in-life': {
        # Select filter example
        'example': {
            'filter_id': 'earliest-language-in-life',
            'selected_values': [
                '0',  # Afrikaans
                '1',  # Albanian
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'earliest-language-in-life',
            'selected_values': [
                '0',  # Afrikaans
                '1',  # Albanian
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Afrikaans
                '1': 1,  # Equal weighting for Albanian
            }
        },
    },

    # Decision-making responsibilities
    'decision-making-responsibilities': {
        # Select filter example
        'example': {
            'filter_id': 'decision-making-responsibilities',
            'selected_values': [
                '0',  # Accounts/finance
                '1',  # Business strategy
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'decision-making-responsibilities',
            'selected_values': [
                '0',  # Accounts/finance
                '1',  # Business strategy
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Accounts/finance
                '1': 1,  # Equal weighting for Business strategy
            }
        },
    },

    # Assistive Technology
    'assistive-technology': {
        # Select filter example
        'example': {
            'filter_id': 'assistive-technology',
            'selected_values': [
                '0',  # Screen reader
                '1',  # Adaptive keyboard
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'assistive-technology',
            'selected_values': [
                '0',  # Screen reader
                '1',  # Adaptive keyboard
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Screen reader
                '1': 1,  # Equal weighting for Adaptive keyboard
            }
        },
    },

    # NFT experience
    'nft-experience': {
        # Select filter example
        'example': {
            'filter_id': 'nft-experience',
            'selected_values': [
                '0',  # I own one or more NFTs
                '1',  # I have created one or more NFTs
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'nft-experience',
            'selected_values': [
                '0',  # I own one or more NFTs
                '1',  # I have created one or more NFTs
            ],
            'weightings': {
                '0': 1,  # Equal weighting for I own one or more NFTs
                '1': 1,  # Equal weighting for I have created one or more NFTs
            }
        },
    },

    # Cloud storage solutions
    'cloud-storage-solutions': {
        # Select filter example
        'example': {
            'filter_id': 'cloud-storage-solutions',
            'selected_values': [
                '0',  # Amazon Cloud Drive
                '1',  # Backblaze
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'cloud-storage-solutions',
            'selected_values': [
                '0',  # Amazon Cloud Drive
                '1',  # Backblaze
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Amazon Cloud Drive
                '1': 1,  # Equal weighting for Backblaze
            }
        },
    },

    # Type of musical instrument(s)
    'type-of-musical-instruments': {
        # Select filter example
        'example': {
            'filter_id': 'type-of-musical-instruments',
            'selected_values': [
                '0',  # Accordion
                '1',  # Afghani guitar
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'type-of-musical-instruments',
            'selected_values': [
                '0',  # Accordion
                '1',  # Afghani guitar
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Accordion
                '1': 1,  # Equal weighting for Afghani guitar
            }
        },
    },

    # Studying abroad
    'studying-abroad': {
        # Select filter example
        'example': {
            'filter_id': 'studying-abroad',
            'selected_values': [
                '0',  # Afghanistan
                '1',  # Aland Islands
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'studying-abroad',
            'selected_values': [
                '0',  # Afghanistan
                '1',  # Aland Islands
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Afghanistan
                '1': 1,  # Equal weighting for Aland Islands
            }
        },
    },

    # Employment in UK Services
    'employment-in-uk-services': {
        # Select filter example
        'example': {
            'filter_id': 'employment-in-uk-services',
            'selected_values': [
                '0',  # 4x4 Response
                '1',  # Ambulance Service
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'employment-in-uk-services',
            'selected_values': [
                '0',  # 4x4 Response
                '1',  # Ambulance Service
            ],
            'weightings': {
                '0': 1,  # Equal weighting for 4x4 Response
                '1': 1,  # Equal weighting for Ambulance Service
            }
        },
    },

    # Alcohol preferences
    'alcohol-preferences': {
        # Select filter example
        'example': {
            'filter_id': 'alcohol-preferences',
            'selected_values': [
                '0',  # Beer (incl. lager, ale, etc.)
                '1',  # Whiskey
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'alcohol-preferences',
            'selected_values': [
                '0',  # Beer (incl. lager, ale, etc.)
                '1',  # Whiskey
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Beer (incl. lager, ale, etc.)
                '1': 1,  # Equal weighting for Whiskey
            }
        },
    },

    # Active subscriptions
    'active-subscriptions': {
        # Select filter example
        'example': {
            'filter_id': 'active-subscriptions',
            'selected_values': [
                '0',  # Media (e.g. Gaming, Movies, Music, Books)
                '1',  # Personal Development (e.g. Languages, Crafts, Fitness, Meditation)
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'active-subscriptions',
            'selected_values': [
                '0',  # Media (e.g. Gaming, Movies, Music, Books)
                '1',  # Personal Development (e.g. Languages, Crafts, Fitness, Meditation)
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Media (e.g. Gaming, Movies, Music, Books)
                '1': 1,  # Equal weighting for Personal Development (e.g. Languages, Crafts, Fitness, Meditation)
            }
        },
    },

    # Insurance types
    'insurance-types': {
        # Select filter example
        'example': {
            'filter_id': 'insurance-types',
            'selected_values': [
                '0',  # Health Insurance
                '1',  # Home Insurance
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'insurance-types',
            'selected_values': [
                '0',  # Health Insurance
                '1',  # Home Insurance
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Health Insurance
                '1': 1,  # Equal weighting for Home Insurance
            }
        },
    },

    # Listening habits while driving
    'listening-habits-while-driving': {
        # Select filter example
        'example': {
            'filter_id': 'listening-habits-while-driving',
            'selected_values': [
                '0',  # AM/FM Radio
                '1',  # Spotify
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'listening-habits-while-driving',
            'selected_values': [
                '0',  # AM/FM Radio
                '1',  # Spotify
            ],
            'weightings': {
                '0': 1,  # Equal weighting for AM/FM Radio
                '1': 1,  # Equal weighting for Spotify
            }
        },
    },

    # Programming Languages
    'programming-languages': {
        # Select filter example
        'example': {
            'filter_id': 'programming-languages',
            'selected_values': [
                '0',  # C#
                '1',  # C and C++
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'programming-languages',
            'selected_values': [
                '0',  # C#
                '1',  # C and C++
            ],
            'weightings': {
                '0': 1,  # Equal weighting for C#
                '1': 1,  # Equal weighting for C and C++
            }
        },
    },

    # Business Travel
    'business-travel': {
        # Select filter example
        'example': {
            'filter_id': 'business-travel',
            'selected_values': [
                '0',  # I regularly hire a car for business travel (5+ times a year)
                '1',  # I own a car that I use for business travel
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'business-travel',
            'selected_values': [
                '0',  # I regularly hire a car for business travel (5+ times a year)
                '1',  # I own a car that I use for business travel
            ],
            'weightings': {
                '0': 1,  # Equal weighting for I regularly hire a car for business travel (5+ times a year)
                '1': 1,  # Equal weighting for I own a car that I use for business travel
            }
        },
    },

    # Mental Health Treatment
    'mental-health-treatment': {
        # Select filter example
        'example': {
            'filter_id': 'mental-health-treatment',
            'selected_values': [
                '0',  # Psychological therapy
                '1',  # Medication
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'mental-health-treatment',
            'selected_values': [
                '0',  # Psychological therapy
                '1',  # Medication
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Psychological therapy
                '1': 1,  # Equal weighting for Medication
            }
        },
    },

    # Chronic condition/illness details
    'chronic-conditionillness-details': {
        # Select filter example
        'example': {
            'filter_id': 'chronic-conditionillness-details',
            'selected_values': [
                '0',  # Parkinson's Disease
                '1',  # Huntington's Disease
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'chronic-conditionillness-details',
            'selected_values': [
                '0',  # Parkinson's Disease
                '1',  # Huntington's Disease
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Parkinson's Disease
                '1': 1,  # Equal weighting for Huntington's Disease
            }
        },
    },

    # Function in Organization
    'function-in-organization': {
        # Select filter example
        'example': {
            'filter_id': 'function-in-organization',
            'selected_values': [
                '0',  # Account Management
                '1',  # Administration/ Personal Assistant
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'function-in-organization',
            'selected_values': [
                '0',  # Account Management
                '1',  # Administration/ Personal Assistant
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Account Management
                '1': 1,  # Equal weighting for Administration/ Personal Assistant
            }
        },
    },

    # Buy now Pay Later - Financial services usage
    'buy-now-pay-later-financial-services-usage': {
        # Select filter example
        'example': {
            'filter_id': 'buy-now-pay-later-financial-services-usage',
            'selected_values': [
                '0',  # Klarna
                '1',  # Paypal
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'buy-now-pay-later-financial-services-usage',
            'selected_values': [
                '0',  # Klarna
                '1',  # Paypal
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Klarna
                '1': 1,  # Equal weighting for Paypal
            }
        },
    },

    # Future House Ownership
    'future-house-ownership': {
        # Select filter example
        'example': {
            'filter_id': 'future-house-ownership',
            'selected_values': [
                '0',  # I am not interested in buying a house at this time.
                '1',  # I am considering buying a house but have not started the process.
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'future-house-ownership',
            'selected_values': [
                '0',  # I am not interested in buying a house at this time.
                '1',  # I am considering buying a house but have not started the process.
            ],
            'weightings': {
                '0': 1,  # Equal weighting for I am not interested in buying a house at this time.
                '1': 1,  # Equal weighting for I am considering buying a house but have not started the process.
            }
        },
    },

    # Short-term let listing
    'short-term-let-listing': {
        # Select filter example
        'example': {
            'filter_id': 'short-term-let-listing',
            'selected_values': [
                '0',  # Airbnb
                '1',  # VRBO
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'short-term-let-listing',
            'selected_values': [
                '0',  # Airbnb
                '1',  # VRBO
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Airbnb
                '1': 1,  # Equal weighting for VRBO
            }
        },
    },

    # Credit card signup reason
    'credit-card-signup-reason': {
        # Select filter example
        'example': {
            'filter_id': 'credit-card-signup-reason',
            'selected_values': [
                '0',  # To earn rewards points or cash back
                '1',  # For a specific purchase or to manage spending
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'credit-card-signup-reason',
            'selected_values': [
                '0',  # To earn rewards points or cash back
                '1',  # For a specific purchase or to manage spending
            ],
            'weightings': {
                '0': 1,  # Equal weighting for To earn rewards points or cash back
                '1': 1,  # Equal weighting for For a specific purchase or to manage spending
            }
        },
    },

    # AI Chatbots
    'ai-chatbots': {
        # Select filter example
        'example': {
            'filter_id': 'ai-chatbots',
            'selected_values': [
                '0',  # Character.AI
                '1',  # ChatGPT
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'ai-chatbots',
            'selected_values': [
                '0',  # Character.AI
                '1',  # ChatGPT
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Character.AI
                '1': 1,  # Equal weighting for ChatGPT
            }
        },
    },

    # Mental Health Diagnosis Detail
    'mental-health-diagnosis-detail': {
        # Select filter example
        'example': {
            'filter_id': 'mental-health-diagnosis-detail',
            'selected_values': [
                '0',  # Anxiety
                '1',  # Attention Deficit Hyperactivity Disorder (ADHD)
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'mental-health-diagnosis-detail',
            'selected_values': [
                '0',  # Anxiety
                '1',  # Attention Deficit Hyperactivity Disorder (ADHD)
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Anxiety
                '1': 1,  # Equal weighting for Attention Deficit Hyperactivity Disorder (ADHD)
            }
        },
    },

    # Online shopping memberships
    'online-shopping-memberships': {
        # Select filter example
        'example': {
            'filter_id': 'online-shopping-memberships',
            'selected_values': [
                '0',  # Amazon Prime
                '1',  # Walmart+
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'online-shopping-memberships',
            'selected_values': [
                '0',  # Amazon Prime
                '1',  # Walmart+
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Amazon Prime
                '1': 1,  # Equal weighting for Walmart+
            }
        },
    },

    # Canadian Main Bank Account 
    'canadian-main-bank-account': {
        # Select filter example
        'example': {
            'filter_id': 'canadian-main-bank-account',
            'selected_values': [
                '0',  # CIBC
                '1',  # Simplii
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'canadian-main-bank-account',
            'selected_values': [
                '0',  # CIBC
                '1',  # Simplii
            ],
            'weightings': {
                '0': 1,  # Equal weighting for CIBC
                '1': 1,  # Equal weighting for Simplii
            }
        },
    },

    # E-learning platform of choice
    'e-learning-platform-of-choice': {
        # Select filter example
        'example': {
            'filter_id': 'e-learning-platform-of-choice',
            'selected_values': [
                '0',  # Masterclass
                '1',  # BBC Maestro
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'e-learning-platform-of-choice',
            'selected_values': [
                '0',  # Masterclass
                '1',  # BBC Maestro
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Masterclass
                '1': 1,  # Equal weighting for BBC Maestro
            }
        },
    },

    # Roles - Primary/Secondary (K-12)
    'roles-primarysecondary-k-12': {
        # Select filter example
        'example': {
            'filter_id': 'roles-primarysecondary-k-12',
            'selected_values': [
                '0',  # State-Level Administrator
                '1',  # Superintendent/Asst. Superintendent
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'roles-primarysecondary-k-12',
            'selected_values': [
                '0',  # State-Level Administrator
                '1',  # Superintendent/Asst. Superintendent
            ],
            'weightings': {
                '0': 1,  # Equal weighting for State-Level Administrator
                '1': 1,  # Equal weighting for Superintendent/Asst. Superintendent
            }
        },
    },

    # Grades supported - Primary/Secondary (K-12)
    'grades-supported-primarysecondary-k-12': {
        # Select filter example
        'example': {
            'filter_id': 'grades-supported-primarysecondary-k-12',
            'selected_values': [
                '0',  # Kindergarten
                '1',  # 1st grade
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'grades-supported-primarysecondary-k-12',
            'selected_values': [
                '0',  # Kindergarten
                '1',  # 1st grade
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Kindergarten
                '1': 1,  # Equal weighting for 1st grade
            }
        },
    },

    # Subjects supported - Primary/Secondary (K-12)
    'subjects-supported-primarysecondary-k-12': {
        # Select filter example
        'example': {
            'filter_id': 'subjects-supported-primarysecondary-k-12',
            'selected_values': [
                '0',  # All subjects
                '1',  # Math
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'subjects-supported-primarysecondary-k-12',
            'selected_values': [
                '0',  # All subjects
                '1',  # Math
            ],
            'weightings': {
                '0': 1,  # Equal weighting for All subjects
                '1': 1,  # Equal weighting for Math
            }
        },
    },

    # Subjects taught - Primary/Secondary (K-12)
    'subjects-taught-primarysecondary-k-12': {
        # Select filter example
        'example': {
            'filter_id': 'subjects-taught-primarysecondary-k-12',
            'selected_values': [
                '0',  # Math
                '1',  # Science
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'subjects-taught-primarysecondary-k-12',
            'selected_values': [
                '0',  # Math
                '1',  # Science
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Math
                '1': 1,  # Equal weighting for Science
            }
        },
    },

    # Banking Products
    'banking-products': {
        # Select filter example
        'example': {
            'filter_id': 'banking-products',
            'selected_values': [
                '0',  # Current/Chequing Account
                '1',  # Savings
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'banking-products',
            'selected_values': [
                '0',  # Current/Chequing Account
                '1',  # Savings
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Current/Chequing Account
                '1': 1,  # Equal weighting for Savings
            }
        },
    },

    # Speech Disorders
    'speech-disorders': {
        # Select filter example
        'example': {
            'filter_id': 'speech-disorders',
            'selected_values': [
                '0',  # Yes (Articulation)
                '1',  # Yes (Voice)
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'speech-disorders',
            'selected_values': [
                '0',  # Yes (Articulation)
                '1',  # Yes (Voice)
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes (Articulation)
                '1': 1,  # Equal weighting for Yes (Voice)
            }
        },
    },

    # Discovering new walks
    'discovering-new-walks': {
        # Select filter example
        'example': {
            'filter_id': 'discovering-new-walks',
            'selected_values': [
                '0',  # AllTrails
                '1',  # Komoot
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'discovering-new-walks',
            'selected_values': [
                '0',  # AllTrails
                '1',  # Komoot
            ],
            'weightings': {
                '0': 1,  # Equal weighting for AllTrails
                '1': 1,  # Equal weighting for Komoot
            }
        },
    },

    # What Sports Do You Watch 
    'what-sports-do-you-watch': {
        # Select filter example
        'example': {
            'filter_id': 'what-sports-do-you-watch',
            'selected_values': [
                '0',  # Soccer / Association Football
                '1',  # Cricket
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'what-sports-do-you-watch',
            'selected_values': [
                '0',  # Soccer / Association Football
                '1',  # Cricket
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Soccer / Association Football
                '1': 1,  # Equal weighting for Cricket
            }
        },
    },

    # Online Gambling Sites (UK)
    'online-gambling-sites-uk': {
        # Select filter example
        'example': {
            'filter_id': 'online-gambling-sites-uk',
            'selected_values': [
                '0',  # 888sport
                '1',  # Bet365
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'online-gambling-sites-uk',
            'selected_values': [
                '0',  # 888sport
                '1',  # Bet365
            ],
            'weightings': {
                '0': 1,  # Equal weighting for 888sport
                '1': 1,  # Equal weighting for Bet365
            }
        },
    },

    # Video Streaming Devices 
    'video-streaming-devices': {
        # Select filter example
        'example': {
            'filter_id': 'video-streaming-devices',
            'selected_values': [
                '0',  # Roku
                '1',  # Amazon Fire TV Stick
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'video-streaming-devices',
            'selected_values': [
                '0',  # Roku
                '1',  # Amazon Fire TV Stick
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Roku
                '1': 1,  # Equal weighting for Amazon Fire TV Stick
            }
        },
    },

    # South Africa Main Bank Account
    'south-africa-main-bank-account': {
        # Select filter example
        'example': {
            'filter_id': 'south-africa-main-bank-account',
            'selected_values': [
                '0',  # ABSA Bank
                '1',  # African Bank Limited
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'south-africa-main-bank-account',
            'selected_values': [
                '0',  # ABSA Bank
                '1',  # African Bank Limited
            ],
            'weightings': {
                '0': 1,  # Equal weighting for ABSA Bank
                '1': 1,  # Equal weighting for African Bank Limited
            }
        },
    },

    # Fluent Sign Languages
    'fluent-sign-languages': {
        # Select filter example
        'example': {
            'filter_id': 'fluent-sign-languages',
            'selected_values': [
                '0',  # American Sign Language (ASL)
                '1',  # British Sign Language (BSL)
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'fluent-sign-languages',
            'selected_values': [
                '0',  # American Sign Language (ASL)
                '1',  # British Sign Language (BSL)
            ],
            'weightings': {
                '0': 1,  # Equal weighting for American Sign Language (ASL)
                '1': 1,  # Equal weighting for British Sign Language (BSL)
            }
        },
    },

    # Age
    'age': {
        # Range filter example
        'example': {
            'filter_id': 'age',
            'selected_range': {
                'lower': 18,
                'upper': 100
            }
        },
        # Age range filter with weightings example
        'weighted_example': {
            'filter_id': 'age',
            'selected_range': {
                'lower': 18,
                'upper': 100
            },
            'weightings': {
                '0': {
                    'selected_range': {
                        'lower': 18,
                        'upper': 30
                    },
                    'weighting': 1
                },
                '1': {
                    'selected_range': {
                        'lower': 31,
                        'upper': 50
                    },
                    'weighting': 1
                }
            }
        },
    },

    # Personal Income (GBP)
    'personal-income-gbp': {
        # Select filter example
        'example': {
            'filter_id': 'personal-income-gbp',
            'selected_values': [
                '0',  # Less than £10,000
                '1',  # £10,000 - £19,999
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'personal-income-gbp',
            'selected_values': [
                '0',  # Less than £10,000
                '1',  # £10,000 - £19,999
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Less than £10,000
                '1': 1,  # Equal weighting for £10,000 - £19,999
            }
        },
    },

    # Mono/multi cultural
    'monomulti-cultural': {
        # Select filter example
        'example': {
            'filter_id': 'monomulti-cultural',
            'selected_values': [
                '0',  # I identify myself as a monocultural individual
                '1',  # I identify myself as a multicultural individual
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'monomulti-cultural',
            'selected_values': [
                '0',  # I identify myself as a monocultural individual
                '1',  # I identify myself as a multicultural individual
            ],
            'weightings': {
                '0': 1,  # Equal weighting for I identify myself as a monocultural individual
                '1': 1,  # Equal weighting for I identify myself as a multicultural individual
            }
        },
    },

    # Medication use
    'medication-use': {
        # Select filter example
        'example': {
            'filter_id': 'medication-use',
            'selected_values': [
                '0',  # No
                '1',  # Prefer not to say
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'medication-use',
            'selected_values': [
                '0',  # No
                '1',  # Prefer not to say
            ],
            'weightings': {
                '0': 1,  # Equal weighting for No
                '1': 1,  # Equal weighting for Prefer not to say
            }
        },
    },

    # Ethnicity (Simplified)
    'ethnicity-simplified': {
        # Select filter example
        'example': {
            'filter_id': 'ethnicity-simplified',
            'selected_values': [
                '0',  # White
                '1',  # Black
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'ethnicity-simplified',
            'selected_values': [
                '0',  # White
                '1',  # Black
            ],
            'weightings': {
                '0': 1,  # Equal weighting for White
                '1': 1,  # Equal weighting for Black
            }
        },
    },

    # Smoking: Tobacco or e-cigarettes
    'smoking-tobacco-or-e-cigarettes': {
        # Select filter example
        'example': {
            'filter_id': 'smoking-tobacco-or-e-cigarettes',
            'selected_values': [
                '0',  # Regularly use both tobacco products and e-cigarettes
                '1',  # Previously smoked tobacco products. Now only use e-cigarettes
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'smoking-tobacco-or-e-cigarettes',
            'selected_values': [
                '0',  # Regularly use both tobacco products and e-cigarettes
                '1',  # Previously smoked tobacco products. Now only use e-cigarettes
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Regularly use both tobacco products and e-cigarettes
                '1': 1,  # Equal weighting for Previously smoked tobacco products. Now only use e-cigarettes
            }
        },
    },

    # Driving licence
    'driving-licence': {
        # Select filter example
        'example': {
            'filter_id': 'driving-licence',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'driving-licence',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Employment Sector within Medicine/Healthcare
    'employment-sector-within-medicinehealthcare': {
        # Select filter example
        'example': {
            'filter_id': 'employment-sector-within-medicinehealthcare',
            'selected_values': [
                '0',  # Doctor
                '1',  # Emergency 911 Dispatcher
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'employment-sector-within-medicinehealthcare',
            'selected_values': [
                '0',  # Doctor
                '1',  # Emergency 911 Dispatcher
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Doctor
                '1': 1,  # Equal weighting for Emergency 911 Dispatcher
            }
        },
    },

    # Head Injury
    'head-injury': {
        # Select filter example
        'example': {
            'filter_id': 'head-injury',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'head-injury',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Computer operating system
    'computer-operating-system': {
        # Select filter example
        'example': {
            'filter_id': 'computer-operating-system',
            'selected_values': [
                '0',  # Chrome OS
                '1',  # macOS
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'computer-operating-system',
            'selected_values': [
                '0',  # Chrome OS
                '1',  # macOS
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Chrome OS
                '1': 1,  # Equal weighting for macOS
            }
        },
    },

    # Handedness
    'handedness': {
        # Select filter example
        'example': {
            'filter_id': 'handedness',
            'selected_values': [
                '0',  # Right-handed
                '1',  # Left-handed
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'handedness',
            'selected_values': [
                '0',  # Right-handed
                '1',  # Left-handed
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Right-handed
                '1': 1,  # Equal weighting for Left-handed
            }
        },
    },

    # UK area of birth
    'uk-area-of-birth': {
        # Select filter example
        'example': {
            'filter_id': 'uk-area-of-birth',
            'selected_values': [
                '0',  # North East, England    (Tees Valley, Durham, Northumberland and Tyne and Wear)
                '1',  # North West, England (Cumbria, Greater Manchester, Lancashire, Merseyside)
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'uk-area-of-birth',
            'selected_values': [
                '0',  # North East, England    (Tees Valley, Durham, Northumberland and Tyne and Wear)
                '1',  # North West, England (Cumbria, Greater Manchester, Lancashire, Merseyside)
            ],
            'weightings': {
                '0': 1,  # Equal weighting for North East, England    (Tees Valley, Durham, Northumberland and Tyne and Wear)
                '1': 1,  # Equal weighting for North West, England (Cumbria, Greater Manchester, Lancashire, Merseyside)
            }
        },
    },

    # Diet
    'diet': {
        # Select filter example
        'example': {
            'filter_id': 'diet',
            'selected_values': [
                '0',  # I do not follow any diet
                '1',  # Vegetarian Diet (you refrain from the consumption of meat (red meat, poultry, seafood, insects and the flesh of any other animal)
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'diet',
            'selected_values': [
                '0',  # I do not follow any diet
                '1',  # Vegetarian Diet (you refrain from the consumption of meat (red meat, poultry, seafood, insects and the flesh of any other animal)
            ],
            'weightings': {
                '0': 1,  # Equal weighting for I do not follow any diet
                '1': 1,  # Equal weighting for Vegetarian Diet (you refrain from the consumption of meat (red meat, poultry, seafood, insects and the flesh of any other animal)
            }
        },
    },

    # Mild cognitive impairment/Dementia
    'mild-cognitive-impairmentdementia': {
        # Select filter example
        'example': {
            'filter_id': 'mild-cognitive-impairmentdementia',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'mild-cognitive-impairmentdementia',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Online shopping
    'online-shopping': {
        # Select filter example
        'example': {
            'filter_id': 'online-shopping',
            'selected_values': [
                '0',  # More than once a week
                '1',  # About once per week
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'online-shopping',
            'selected_values': [
                '0',  # More than once a week
                '1',  # About once per week
            ],
            'weightings': {
                '0': 1,  # Equal weighting for More than once a week
                '1': 1,  # Equal weighting for About once per week
            }
        },
    },

    # Non-Religious
    'non-religious': {
        # Select filter example
        'example': {
            'filter_id': 'non-religious',
            'selected_values': [
                '0',  # Agnostic
                '1',  # Atheist
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'non-religious',
            'selected_values': [
                '0',  # Agnostic
                '1',  # Atheist
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Agnostic
                '1': 1,  # Equal weighting for Atheist
            }
        },
    },

    # Negotiation Experience
    'negotiation-experience': {
        # Select filter example
        'example': {
            'filter_id': 'negotiation-experience',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'negotiation-experience',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Corrected vision
    'corrected-vision': {
        # Select filter example
        'example': {
            'filter_id': 'corrected-vision',
            'selected_values': [
                '0',  # I mainly use glasses
                '1',  # I mainly use contact lenses
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'corrected-vision',
            'selected_values': [
                '0',  # I mainly use glasses
                '1',  # I mainly use contact lenses
            ],
            'weightings': {
                '0': 1,  # Equal weighting for I mainly use glasses
                '1': 1,  # Equal weighting for I mainly use contact lenses
            }
        },
    },

    # Smoking status
    'smoking-status': {
        # Select filter example
        'example': {
            'filter_id': 'smoking-status',
            'selected_values': [
                '0',  # I am a current smoker (smoke at least 5 cigarettes a day and have smoked this amount for at least one year)
                '1',  # I am a recent smoker (smoke at least 5 cigarettes a day and have smoked this amount for less than one year)
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'smoking-status',
            'selected_values': [
                '0',  # I am a current smoker (smoke at least 5 cigarettes a day and have smoked this amount for at least one year)
                '1',  # I am a recent smoker (smoke at least 5 cigarettes a day and have smoked this amount for less than one year)
            ],
            'weightings': {
                '0': 1,  # Equal weighting for I am a current smoker (smoke at least 5 cigarettes a day and have smoked this amount for at least one year)
                '1': 1,  # Equal weighting for I am a recent smoker (smoke at least 5 cigarettes a day and have smoked this amount for less than one year)
            }
        },
    },

    # Number of subordinates
    'number-of-subordinates': {
        # Select filter example
        'example': {
            'filter_id': 'number-of-subordinates',
            'selected_values': [
                '0',  # 1
                '1',  # 2-3
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'number-of-subordinates',
            'selected_values': [
                '0',  # 1
                '1',  # 2-3
            ],
            'weightings': {
                '0': 1,  # Equal weighting for 1
                '1': 1,  # Equal weighting for 2-3
            }
        },
    },

    # Investment
    'investment': {
        # Select filter example
        'example': {
            'filter_id': 'investment',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'investment',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Political Affiliation (UK)
    'political-affiliation-uk': {
        # Select filter example
        'example': {
            'filter_id': 'political-affiliation-uk',
            'selected_values': [
                '0',  # Left
                '1',  # Centre
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'political-affiliation-uk',
            'selected_values': [
                '0',  # Left
                '1',  # Centre
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Left
                '1': 1,  # Equal weighting for Centre
            }
        },
    },

    # ProLife/ProChoice
    'prolifeprochoice': {
        # Select filter example
        'example': {
            'filter_id': 'prolifeprochoice',
            'selected_values': [
                '0',  # Pro-Life
                '1',  # Pro-choice
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'prolifeprochoice',
            'selected_values': [
                '0',  # Pro-Life
                '1',  # Pro-choice
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Pro-Life
                '1': 1,  # Equal weighting for Pro-choice
            }
        },
    },

    # US Presidential election
    'us-presidential-election': {
        # Select filter example
        'example': {
            'filter_id': 'us-presidential-election',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'us-presidential-election',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Employment Sector within Business Management and Administration
    'employment-sector-within-business-management-and-administration': {
        # Select filter example
        'example': {
            'filter_id': 'employment-sector-within-business-management-and-administration',
            'selected_values': [
                '0',  # Accountant
                '1',  # Administrative Assistant/Secretary
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'employment-sector-within-business-management-and-administration',
            'selected_values': [
                '0',  # Accountant
                '1',  # Administrative Assistant/Secretary
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Accountant
                '1': 1,  # Equal weighting for Administrative Assistant/Secretary
            }
        },
    },

    # Groceries online
    'groceries-online': {
        # Select filter example
        'example': {
            'filter_id': 'groceries-online',
            'selected_values': [
                '0',  # More than once a week
                '1',  # About once per week
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'groceries-online',
            'selected_values': [
                '0',  # More than once a week
                '1',  # About once per week
            ],
            'weightings': {
                '0': 1,  # Equal weighting for More than once a week
                '1': 1,  # Equal weighting for About once per week
            }
        },
    },

    # Primary Grocery Shopper
    'primary-grocery-shopper': {
        # Select filter example
        'example': {
            'filter_id': 'primary-grocery-shopper',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'primary-grocery-shopper',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Industry
    'industry': {
        # Select filter example
        'example': {
            'filter_id': 'industry',
            'selected_values': [
                '0',  # Agriculture Forestry Fishing and Hunting
                '1',  # Arts Design Entertainment and Recreation
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'industry',
            'selected_values': [
                '0',  # Agriculture Forestry Fishing and Hunting
                '1',  # Arts Design Entertainment and Recreation
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Agriculture Forestry Fishing and Hunting
                '1': 1,  # Equal weighting for Arts Design Entertainment and Recreation
            }
        },
    },

    # Weekly device usage
    'weekly-device-usage': {
        # Select filter example
        'example': {
            'filter_id': 'weekly-device-usage',
            'selected_values': [
                '0',  # Never
                '1',  # Once a week
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'weekly-device-usage',
            'selected_values': [
                '0',  # Never
                '1',  # Once a week
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Never
                '1': 1,  # Equal weighting for Once a week
            }
        },
    },

    # Number of romantic partners
    'number-of-romantic-partners': {
        # Select filter example
        'example': {
            'filter_id': 'number-of-romantic-partners',
            'selected_values': [
                '0',  # 0
                '1',  # 1
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'number-of-romantic-partners',
            'selected_values': [
                '0',  # 0
                '1',  # 1
            ],
            'weightings': {
                '0': 1,  # Equal weighting for 0
                '1': 1,  # Equal weighting for 1
            }
        },
    },

    # Autism Spectrum Disorder
    'autism-spectrum-disorder': {
        # Select filter example
        'example': {
            'filter_id': 'autism-spectrum-disorder',
            'selected_values': [
                '0',  # Yes - as a child
                '1',  # Yes - as an adult
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'autism-spectrum-disorder',
            'selected_values': [
                '0',  # Yes - as a child
                '1',  # Yes - as an adult
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes - as a child
                '1': 1,  # Equal weighting for Yes - as an adult
            }
        },
    },

    # Technology use at work
    'technology-use-at-work': {
        # Select filter example
        'example': {
            'filter_id': 'technology-use-at-work',
            'selected_values': [
                '0',  # not at all
                '1',  # less than once a week
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'technology-use-at-work',
            'selected_values': [
                '0',  # not at all
                '1',  # less than once a week
            ],
            'weightings': {
                '0': 1,  # Equal weighting for not at all
                '1': 1,  # Equal weighting for less than once a week
            }
        },
    },

    # Number of children
    'number-of-children': {
        # Select filter example
        'example': {
            'filter_id': 'number-of-children',
            'selected_values': [
                '0',  # 1
                '1',  # 2
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'number-of-children',
            'selected_values': [
                '0',  # 1
                '1',  # 2
            ],
            'weightings': {
                '0': 1,  # Equal weighting for 1
                '1': 1,  # Equal weighting for 2
            }
        },
    },

    # Long-term health condition/disability
    'long-term-health-conditiondisability': {
        # Select filter example
        'example': {
            'filter_id': 'long-term-health-conditiondisability',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'long-term-health-conditiondisability',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Confidentiality agreement
    'confidentiality-agreement': {
        # Select filter example
        'example': {
            'filter_id': 'confidentiality-agreement',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'confidentiality-agreement',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Phone Operating System
    'phone-operating-system': {
        # Select filter example
        'example': {
            'filter_id': 'phone-operating-system',
            'selected_values': [
                '0',  # Android
                '1',  # iOS (iPhone)
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'phone-operating-system',
            'selected_values': [
                '0',  # Android
                '1',  # iOS (iPhone)
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Android
                '1': 1,  # Equal weighting for iOS (iPhone)
            }
        },
    },

    # Living abroad
    'living-abroad': {
        # Select filter example
        'example': {
            'filter_id': 'living-abroad',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'living-abroad',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Dating apps
    'dating-apps': {
        # Select filter example
        'example': {
            'filter_id': 'dating-apps',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'dating-apps',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Sexual partner
    'sexual-partner': {
        # Select filter example
        'example': {
            'filter_id': 'sexual-partner',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'sexual-partner',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Moved with partner
    'moved-with-partner': {
        # Select filter example
        'example': {
            'filter_id': 'moved-with-partner',
            'selected_values': [
                '0',  # Yes we did - primarily for me
                '1',  # Yes we did - primarily for my partner
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'moved-with-partner',
            'selected_values': [
                '0',  # Yes we did - primarily for me
                '1',  # Yes we did - primarily for my partner
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes we did - primarily for me
                '1': 1,  # Equal weighting for Yes we did - primarily for my partner
            }
        },
    },

    # Leadership/Position of power/Supervisory duties
    'leadershipposition-of-powersupervisory-duties': {
        # Select filter example
        'example': {
            'filter_id': 'leadershipposition-of-powersupervisory-duties',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'leadershipposition-of-powersupervisory-duties',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Student Status
    'student-status': {
        # Select filter example
        'example': {
            'filter_id': 'student-status',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'student-status',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Other crowdsourcing platforms
    'other-crowdsourcing-platforms': {
        # Select filter example
        'example': {
            'filter_id': 'other-crowdsourcing-platforms',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'other-crowdsourcing-platforms',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Alcohol therapy
    'alcohol-therapy': {
        # Select filter example
        'example': {
            'filter_id': 'alcohol-therapy',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'alcohol-therapy',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Android OS version
    'android-os-version': {
        # Select filter example
        'example': {
            'filter_id': 'android-os-version',
            'selected_values': [
                '0',  # KitKat
                '1',  # Lollipop
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'android-os-version',
            'selected_values': [
                '0',  # KitKat
                '1',  # Lollipop
            ],
            'weightings': {
                '0': 1,  # Equal weighting for KitKat
                '1': 1,  # Equal weighting for Lollipop
            }
        },
    },

    # English speaking Monolingual
    'english-speaking-monolingual': {
        # Select filter example
        'example': {
            'filter_id': 'english-speaking-monolingual',
            'selected_values': [
                '0',  # I only know English
                '1',  # I know one other language in addition to English
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'english-speaking-monolingual',
            'selected_values': [
                '0',  # I only know English
                '1',  # I know one other language in addition to English
            ],
            'weightings': {
                '0': 1,  # Equal weighting for I only know English
                '1': 1,  # Equal weighting for I know one other language in addition to English
            }
        },
    },

    # Management experience
    'management-experience': {
        # Select filter example
        'example': {
            'filter_id': 'management-experience',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'management-experience',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Sex
    'sex': {
        # Select filter example
        'example': {
            'filter_id': 'sex',
            'selected_values': [
                '0',  # Male
                '1',  # Female
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'sex',
            'selected_values': [
                '0',  # Male
                '1',  # Female
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Male
                '1': 1,  # Equal weighting for Female
            }
        },
    },

    # First Language
    'first-language': {
        # Select filter example
        'example': {
            'filter_id': 'first-language',
            'selected_values': [
                '0',  # Afrikaans
                '1',  # Albanian
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'first-language',
            'selected_values': [
                '0',  # Afrikaans
                '1',  # Albanian
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Afrikaans
                '1': 1,  # Equal weighting for Albanian
            }
        },
    },

    # Charitable Giving
    'charitable-giving': {
        # Select filter example
        'example': {
            'filter_id': 'charitable-giving',
            'selected_values': [
                '0',  # £501+
                '1',  # £201-£500
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'charitable-giving',
            'selected_values': [
                '0',  # £501+
                '1',  # £201-£500
            ],
            'weightings': {
                '0': 1,  # Equal weighting for £501+
                '1': 1,  # Equal weighting for £201-£500
            }
        },
    },

    # Ethnicity
    'ethnicity': {
        # Select filter example
        'example': {
            'filter_id': 'ethnicity',
            'selected_values': [
                '0',  # African
                '1',  # Black/African American
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'ethnicity',
            'selected_values': [
                '0',  # African
                '1',  # Black/African American
            ],
            'weightings': {
                '0': 1,  # Equal weighting for African
                '1': 1,  # Equal weighting for Black/African American
            }
        },
    },

    # Siblings
    'siblings': {
        # Select filter example
        'example': {
            'filter_id': 'siblings',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'siblings',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Crime victim
    'crime-victim': {
        # Select filter example
        'example': {
            'filter_id': 'crime-victim',
            'selected_values': [
                '0',  # True
                '1',  # False
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'crime-victim',
            'selected_values': [
                '0',  # True
                '1',  # False
            ],
            'weightings': {
                '0': 1,  # Equal weighting for True
                '1': 1,  # Equal weighting for False
            }
        },
    },

    # iPhone model
    'iphone-model': {
        # Select filter example
        'example': {
            'filter_id': 'iphone-model',
            'selected_values': [
                '0',  # 1st Generation
                '1',  # 3G
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'iphone-model',
            'selected_values': [
                '0',  # 1st Generation
                '1',  # 3G
            ],
            'weightings': {
                '0': 1,  # Equal weighting for 1st Generation
                '1': 1,  # Equal weighting for 3G
            }
        },
    },

    # English Premier League Fan
    'english-premier-league-fan': {
        # Select filter example
        'example': {
            'filter_id': 'english-premier-league-fan',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'english-premier-league-fan',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Chronic Disease
    'chronic-disease': {
        # Select filter example
        'example': {
            'filter_id': 'chronic-disease',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'chronic-disease',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Household Size
    'household-size': {
        # Select filter example
        'example': {
            'filter_id': 'household-size',
            'selected_values': [
                '0',  # 1
                '1',  # 2
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'household-size',
            'selected_values': [
                '0',  # 1
                '1',  # 2
            ],
            'weightings': {
                '0': 1,  # Equal weighting for 1
                '1': 1,  # Equal weighting for 2
            }
        },
    },

    # Charity Affiliation
    'charity-affiliation': {
        # Select filter example
        'example': {
            'filter_id': 'charity-affiliation',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'charity-affiliation',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Trips Abroad
    'trips-abroad': {
        # Select filter example
        'example': {
            'filter_id': 'trips-abroad',
            'selected_values': [
                '0',  # In the last month
                '1',  # In the last 3 months
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'trips-abroad',
            'selected_values': [
                '0',  # In the last month
                '1',  # In the last 3 months
            ],
            'weightings': {
                '0': 1,  # Equal weighting for In the last month
                '1': 1,  # Equal weighting for In the last 3 months
            }
        },
    },

    # Luxury Goods
    'luxury-goods': {
        # Select filter example
        'example': {
            'filter_id': 'luxury-goods',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'luxury-goods',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Entrepreneurship
    'entrepreneurship': {
        # Select filter example
        'example': {
            'filter_id': 'entrepreneurship',
            'selected_values': [
                '0',  # I have in the past
                '1',  # I am currently doing this
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'entrepreneurship',
            'selected_values': [
                '0',  # I have in the past
                '1',  # I am currently doing this
            ],
            'weightings': {
                '0': 1,  # Equal weighting for I have in the past
                '1': 1,  # Equal weighting for I am currently doing this
            }
        },
    },

    # NHS Mental Health Support
    'nhs-mental-health-support': {
        # Select filter example
        'example': {
            'filter_id': 'nhs-mental-health-support',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'nhs-mental-health-support',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Children and technology
    'children-and-technology': {
        # Select filter example
        'example': {
            'filter_id': 'children-and-technology',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'children-and-technology',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Employment-Sector
    'employment-sector': {
        # Select filter example
        'example': {
            'filter_id': 'employment-sector',
            'selected_values': [
                '0',  # Agriculture, Food and Natural Resources
                '1',  # Architecture and Construction
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'employment-sector',
            'selected_values': [
                '0',  # Agriculture, Food and Natural Resources
                '1',  # Architecture and Construction
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Agriculture, Food and Natural Resources
                '1': 1,  # Equal weighting for Architecture and Construction
            }
        },
    },

    # Work week in hours
    'work-week-in-hours': {
        # Select filter example
        'example': {
            'filter_id': 'work-week-in-hours',
            'selected_values': [
                '0',  # 1-10 hours per week
                '1',  # 11-20 hours per week
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'work-week-in-hours',
            'selected_values': [
                '0',  # 1-10 hours per week
                '1',  # 11-20 hours per week
            ],
            'weightings': {
                '0': 1,  # Equal weighting for 1-10 hours per week
                '1': 1,  # Equal weighting for 11-20 hours per week
            }
        },
    },

    # Supervisor
    'supervisor': {
        # Select filter example
        'example': {
            'filter_id': 'supervisor',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'supervisor',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Year of birth of first child
    'year-of-birth-of-first-child': {
        # Select filter example
        'example': {
            'filter_id': 'year-of-birth-of-first-child',
            'selected_values': [
                '0',  # 1900
                '1',  # 1901
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'year-of-birth-of-first-child',
            'selected_values': [
                '0',  # 1900
                '1',  # 1901
            ],
            'weightings': {
                '0': 1,  # Equal weighting for 1900
                '1': 1,  # Equal weighting for 1901
            }
        },
    },

    # Workgroups
    'workgroups': {
        # Select filter example
        'example': {
            'filter_id': 'workgroups',
            'selected_values': [
                '0',  # I work alone
                '1',  # I sometimes work as part of a group and sometimes alone
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'workgroups',
            'selected_values': [
                '0',  # I work alone
                '1',  # I sometimes work as part of a group and sometimes alone
            ],
            'weightings': {
                '0': 1,  # Equal weighting for I work alone
                '1': 1,  # Equal weighting for I sometimes work as part of a group and sometimes alone
            }
        },
    },

    # Teacher
    'teacher': {
        # Select filter example
        'example': {
            'filter_id': 'teacher',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'teacher',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Concern about environmental issues
    'concern-about-environmental-issues': {
        # Select filter example
        'example': {
            'filter_id': 'concern-about-environmental-issues',
            'selected_values': [
                '0',  # 1 (Not at all concerned)
                '1',  # 2
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'concern-about-environmental-issues',
            'selected_values': [
                '0',  # 1 (Not at all concerned)
                '1',  # 2
            ],
            'weightings': {
                '0': 1,  # Equal weighting for 1 (Not at all concerned)
                '1': 1,  # Equal weighting for 2
            }
        },
    },

    # Units of alcohol
    'units-of-alcohol': {
        # Select filter example
        'example': {
            'filter_id': 'units-of-alcohol',
            'selected_values': [
                '0',  # 0
                '1',  # 1-4
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'units-of-alcohol',
            'selected_values': [
                '0',  # 0
                '1',  # 1-4
            ],
            'weightings': {
                '0': 1,  # Equal weighting for 0
                '1': 1,  # Equal weighting for 1-4
            }
        },
    },

    # Vaccine Opinions 2
    'vaccine-opinions-2': {
        # Select filter example
        'example': {
            'filter_id': 'vaccine-opinions-2',
            'selected_values': [
                '0',  # 1 (TOTALLY DISAGREEE)
                '1',  # 2 (DISAGREE)
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'vaccine-opinions-2',
            'selected_values': [
                '0',  # 1 (TOTALLY DISAGREEE)
                '1',  # 2 (DISAGREE)
            ],
            'weightings': {
                '0': 1,  # Equal weighting for 1 (TOTALLY DISAGREEE)
                '1': 1,  # Equal weighting for 2 (DISAGREE)
            }
        },
    },

    # Pregnancy
    'pregnancy': {
        # Select filter example
        'example': {
            'filter_id': 'pregnancy',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'pregnancy',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Car usage
    'car-usage': {
        # Select filter example
        'example': {
            'filter_id': 'car-usage',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'car-usage',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Pregnancy (partners)
    'pregnancy-partners': {
        # Select filter example
        'example': {
            'filter_id': 'pregnancy-partners',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'pregnancy-partners',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Hiring experience
    'hiring-experience': {
        # Select filter example
        'example': {
            'filter_id': 'hiring-experience',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'hiring-experience',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Restricted food intake
    'restricted-food-intake': {
        # Select filter example
        'example': {
            'filter_id': 'restricted-food-intake',
            'selected_values': [
                '0',  # No. I do not currently for at least one week restrict my food intake to manage my weight
                '1',  # Yes. To lose weight
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'restricted-food-intake',
            'selected_values': [
                '0',  # No. I do not currently for at least one week restrict my food intake to manage my weight
                '1',  # Yes. To lose weight
            ],
            'weightings': {
                '0': 1,  # Equal weighting for No. I do not currently for at least one week restrict my food intake to manage my weight
                '1': 1,  # Equal weighting for Yes. To lose weight
            }
        },
    },

    # Socioeconomic Status
    'socioeconomic-status': {
        # Select filter example
        'example': {
            'filter_id': 'socioeconomic-status',
            'selected_values': [
                '0',  # 1
                '1',  # 2
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'socioeconomic-status',
            'selected_values': [
                '0',  # 1
                '1',  # 2
            ],
            'weightings': {
                '0': 1,  # Equal weighting for 1
                '1': 1,  # Equal weighting for 2
            }
        },
    },

    # Windfarms
    'windfarms': {
        # Select filter example
        'example': {
            'filter_id': 'windfarms',
            'selected_values': [
                '0',  # 1
                '1',  # 2
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'windfarms',
            'selected_values': [
                '0',  # 1
                '1',  # 2
            ],
            'weightings': {
                '0': 1,  # Equal weighting for 1
                '1': 1,  # Equal weighting for 2
            }
        },
    },

    # Informal/unpaid caring responsibilities
    'informalunpaid-caring-responsibilities': {
        # Select filter example
        'example': {
            'filter_id': 'informalunpaid-caring-responsibilities',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'informalunpaid-caring-responsibilities',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Number of Siblings
    'number-of-siblings': {
        # Select filter example
        'example': {
            'filter_id': 'number-of-siblings',
            'selected_values': [
                '0',  # 0
                '1',  # 1
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'number-of-siblings',
            'selected_values': [
                '0',  # 0
                '1',  # 1
            ],
            'weightings': {
                '0': 1,  # Equal weighting for 0
                '1': 1,  # Equal weighting for 1
            }
        },
    },

    # Employee interactions
    'employee-interactions': {
        # Select filter example
        'example': {
            'filter_id': 'employee-interactions',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'employee-interactions',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Living with biological child's parent
    'living-with-biological-childs-parent': {
        # Select filter example
        'example': {
            'filter_id': 'living-with-biological-childs-parent',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'living-with-biological-childs-parent',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Weekly Exercise
    'weekly-exercise': {
        # Select filter example
        'example': {
            'filter_id': 'weekly-exercise',
            'selected_values': [
                '0',  # Never (0 – 60 minutes per week)
                '1',  # Sometimes (60 – 150 minutes per week)
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'weekly-exercise',
            'selected_values': [
                '0',  # Never (0 – 60 minutes per week)
                '1',  # Sometimes (60 – 150 minutes per week)
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Never (0 – 60 minutes per week)
                '1': 1,  # Equal weighting for Sometimes (60 – 150 minutes per week)
            }
        },
    },

    # Were you raised monolingual?
    'were-you-raised-monolingual': {
        # Select filter example
        'example': {
            'filter_id': 'were-you-raised-monolingual',
            'selected_values': [
                '0',  # I was raised with my native language only
                '1',  # I was raised with two or more languages
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'were-you-raised-monolingual',
            'selected_values': [
                '0',  # I was raised with my native language only
                '1',  # I was raised with two or more languages
            ],
            'weightings': {
                '0': 1,  # Equal weighting for I was raised with my native language only
                '1': 1,  # Equal weighting for I was raised with two or more languages
            }
        },
    },

    # Remote/office work
    'remoteoffice-work': {
        # Select filter example
        'example': {
            'filter_id': 'remoteoffice-work',
            'selected_values': [
                '0',  # I always work from a central place of work
                '1',  # I sometimes work from a central place of work and sometimes remotely
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'remoteoffice-work',
            'selected_values': [
                '0',  # I always work from a central place of work
                '1',  # I sometimes work from a central place of work and sometimes remotely
            ],
            'weightings': {
                '0': 1,  # Equal weighting for I always work from a central place of work
                '1': 1,  # Equal weighting for I sometimes work from a central place of work and sometimes remotely
            }
        },
    },

    # Mental illness daily impact
    'mental-illness-daily-impact': {
        # Select filter example
        'example': {
            'filter_id': 'mental-illness-daily-impact',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'mental-illness-daily-impact',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Participating together with a romantic partner on Prolific
    'participating-together-with-a-romantic-partner-on-prolific': {
        # Select filter example
        'example': {
            'filter_id': 'participating-together-with-a-romantic-partner-on-prolific',
            'selected_values': [
                '0',  # Yes. I have a romantic partner who has a Prolific account and we would be willing to take part as a couple
                '1',  # No. I either do not have a romantic partner on Prolific or we would not be willing to take part as a couple
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'participating-together-with-a-romantic-partner-on-prolific',
            'selected_values': [
                '0',  # Yes. I have a romantic partner who has a Prolific account and we would be willing to take part as a couple
                '1',  # No. I either do not have a romantic partner on Prolific or we would not be willing to take part as a couple
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes. I have a romantic partner who has a Prolific account and we would be willing to take part as a couple
                '1': 1,  # Equal weighting for No. I either do not have a romantic partner on Prolific or we would not be willing to take part as a couple
            }
        },
    },

    # Vaping status
    'vaping-status': {
        # Select filter example
        'example': {
            'filter_id': 'vaping-status',
            'selected_values': [
                '0',  # I am a non-vaper (vaped fewer than 20 times in my lifetime)
                '1',  # I am a current vaper (vape at least once a day)
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'vaping-status',
            'selected_values': [
                '0',  # I am a non-vaper (vaped fewer than 20 times in my lifetime)
                '1',  # I am a current vaper (vape at least once a day)
            ],
            'weightings': {
                '0': 1,  # Equal weighting for I am a non-vaper (vaped fewer than 20 times in my lifetime)
                '1': 1,  # Equal weighting for I am a current vaper (vape at least once a day)
            }
        },
    },

    # Record Video
    'record-video': {
        # Select filter example
        'example': {
            'filter_id': 'record-video',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'record-video',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Head Injury: Knock out history
    'head-injury-knock-out-history': {
        # Select filter example
        'example': {
            'filter_id': 'head-injury-knock-out-history',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'head-injury-knock-out-history',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Body Mass Index
    'body-mass-index': {
        # Select filter example
        'example': {
            'filter_id': 'body-mass-index',
            'selected_values': [
                '0',  # <20
                '1',  # 20-24.9
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'body-mass-index',
            'selected_values': [
                '0',  # <20
                '1',  # 20-24.9
            ],
            'weightings': {
                '0': 1,  # Equal weighting for <20
                '1': 1,  # Equal weighting for 20-24.9
            }
        },
    },

    # Online Shopping Frequency
    'online-shopping-frequency': {
        # Select filter example
        'example': {
            'filter_id': 'online-shopping-frequency',
            'selected_values': [
                '0',  # More than once a week
                '1',  # About once per week
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'online-shopping-frequency',
            'selected_values': [
                '0',  # More than once a week
                '1',  # About once per week
            ],
            'weightings': {
                '0': 1,  # Equal weighting for More than once a week
                '1': 1,  # Equal weighting for About once per week
            }
        },
    },

    # Prison
    'prison': {
        # Select filter example
        'example': {
            'filter_id': 'prison',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'prison',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Diabetes type
    'diabetes-type': {
        # Select filter example
        'example': {
            'filter_id': 'diabetes-type',
            'selected_values': [
                '0',  # Type 1
                '1',  # Type 2
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'diabetes-type',
            'selected_values': [
                '0',  # Type 1
                '1',  # Type 2
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Type 1
                '1': 1,  # Equal weighting for Type 2
            }
        },
    },

    # Video Games
    'video-games': {
        # Select filter example
        'example': {
            'filter_id': 'video-games',
            'selected_values': [
                '0',  # 0-3 hours
                '1',  # 3-6 hours
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'video-games',
            'selected_values': [
                '0',  # 0-3 hours
                '1',  # 3-6 hours
            ],
            'weightings': {
                '0': 1,  # Equal weighting for 0-3 hours
                '1': 1,  # Equal weighting for 3-6 hours
            }
        },
    },

    # Romantic Relationship
    'romantic-relationship': {
        # Select filter example
        'example': {
            'filter_id': 'romantic-relationship',
            'selected_values': [
                '0',  # Less than/equal to 3 months
                '1',  # Between 4 months and 6 months
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'romantic-relationship',
            'selected_values': [
                '0',  # Less than/equal to 3 months
                '1',  # Between 4 months and 6 months
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Less than/equal to 3 months
                '1': 1,  # Equal weighting for Between 4 months and 6 months
            }
        },
    },

    # Living with spouse/partner
    'living-with-spousepartner': {
        # Select filter example
        'example': {
            'filter_id': 'living-with-spousepartner',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'living-with-spousepartner',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Safety procedures at work
    'safety-procedures-at-work': {
        # Select filter example
        'example': {
            'filter_id': 'safety-procedures-at-work',
            'selected_values': [
                '0',  # My job doesn’t involve the use of safety procedures.
                '1',  # Occasionally my job task requires the use of a safety procedure.
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'safety-procedures-at-work',
            'selected_values': [
                '0',  # My job doesn’t involve the use of safety procedures.
                '1',  # Occasionally my job task requires the use of a safety procedure.
            ],
            'weightings': {
                '0': 1,  # Equal weighting for My job doesn’t involve the use of safety procedures.
                '1': 1,  # Equal weighting for Occasionally my job task requires the use of a safety procedure.
            }
        },
    },

    # Employer Type
    'employer-type': {
        # Select filter example
        'example': {
            'filter_id': 'employer-type',
            'selected_values': [
                '0',  # Employee of a for-profit company or business or of an individual, for wages, salary, or commissions
                '1',  # Employee of a not-for-profit, tax-exempt, or charitable organization
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'employer-type',
            'selected_values': [
                '0',  # Employee of a for-profit company or business or of an individual, for wages, salary, or commissions
                '1',  # Employee of a not-for-profit, tax-exempt, or charitable organization
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Employee of a for-profit company or business or of an individual, for wages, salary, or commissions
                '1': 1,  # Equal weighting for Employee of a not-for-profit, tax-exempt, or charitable organization
            }
        },
    },

    # Nationality (UK)
    'nationality-uk': {
        # Select filter example
        'example': {
            'filter_id': 'nationality-uk',
            'selected_values': [
                '0',  # England
                '1',  # Wales
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'nationality-uk',
            'selected_values': [
                '0',  # England
                '1',  # Wales
            ],
            'weightings': {
                '0': 1,  # Equal weighting for England
                '1': 1,  # Equal weighting for Wales
            }
        },
    },

    # Industry Role
    'industry-role': {
        # Select filter example
        'example': {
            'filter_id': 'industry-role',
            'selected_values': [
                '0',  # Upper Management
                '1',  # Trained Professional
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'industry-role',
            'selected_values': [
                '0',  # Upper Management
                '1',  # Trained Professional
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Upper Management
                '1': 1,  # Equal weighting for Trained Professional
            }
        },
    },

    # Colleague
    'colleague': {
        # Select filter example
        'example': {
            'filter_id': 'colleague',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'colleague',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Customer facing
    'customer-facing': {
        # Select filter example
        'example': {
            'filter_id': 'customer-facing',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'customer-facing',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Respiratory disease
    'respiratory-disease': {
        # Select filter example
        'example': {
            'filter_id': 'respiratory-disease',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'respiratory-disease',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Startup
    'startup': {
        # Select filter example
        'example': {
            'filter_id': 'startup',
            'selected_values': [
                '0',  # No, I've never considered it.
                '1',  # Yes, I've considered it
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'startup',
            'selected_values': [
                '0',  # No, I've never considered it.
                '1',  # Yes, I've considered it
            ],
            'weightings': {
                '0': 1,  # Equal weighting for No, I've never considered it.
                '1': 1,  # Equal weighting for Yes, I've considered it
            }
        },
    },

    # UK general election 2017
    'uk-general-election-2017': {
        # Select filter example
        'example': {
            'filter_id': 'uk-general-election-2017',
            'selected_values': [
                '0',  # I did not vote
                '1',  # Conservatives
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'uk-general-election-2017',
            'selected_values': [
                '0',  # I did not vote
                '1',  # Conservatives
            ],
            'weightings': {
                '0': 1,  # Equal weighting for I did not vote
                '1': 1,  # Equal weighting for Conservatives
            }
        },
    },

    # Nationality
    'nationality': {
        # Select filter example
        'example': {
            'filter_id': 'nationality',
            'selected_values': [
                '0',  # United Kingdom
                '1',  # United States
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'nationality',
            'selected_values': [
                '0',  # United Kingdom
                '1',  # United States
            ],
            'weightings': {
                '0': 1,  # Equal weighting for United Kingdom
                '1': 1,  # Equal weighting for United States
            }
        },
    },

    # Current U.S state of residence
    'current-us-state-of-residence': {
        # Select filter example
        'example': {
            'filter_id': 'current-us-state-of-residence',
            'selected_values': [
                '0',  # Alabama (AL)
                '1',  # Alaska (AK)
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'current-us-state-of-residence',
            'selected_values': [
                '0',  # Alabama (AL)
                '1',  # Alaska (AK)
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Alabama (AL)
                '1': 1,  # Equal weighting for Alaska (AK)
            }
        },
    },

    # Property Type
    'property-type': {
        # Select filter example
        'example': {
            'filter_id': 'property-type',
            'selected_values': [
                '0',  # Apartment/Flat (purpose built block)
                '1',  # Apartment/Flat (converted within other property type such as house)
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'property-type',
            'selected_values': [
                '0',  # Apartment/Flat (purpose built block)
                '1',  # Apartment/Flat (converted within other property type such as house)
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Apartment/Flat (purpose built block)
                '1': 1,  # Equal weighting for Apartment/Flat (converted within other property type such as house)
            }
        },
    },

    # Antidepressants
    'antidepressants': {
        # Select filter example
        'example': {
            'filter_id': 'antidepressants',
            'selected_values': [
                '0',  # Citalopram (Celexa)
                '1',  # Escitalopram (Lexapro)
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'antidepressants',
            'selected_values': [
                '0',  # Citalopram (Celexa)
                '1',  # Escitalopram (Lexapro)
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Citalopram (Celexa)
                '1': 1,  # Equal weighting for Escitalopram (Lexapro)
            }
        },
    },

    # Computer Programming
    'computer-programming': {
        # Select filter example
        'example': {
            'filter_id': 'computer-programming',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'computer-programming',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # BREXIT
    'brexit': {
        # Select filter example
        'example': {
            'filter_id': 'brexit',
            'selected_values': [
                '0',  # Remain
                '1',  # Leave
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'brexit',
            'selected_values': [
                '0',  # Remain
                '1',  # Leave
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Remain
                '1': 1,  # Equal weighting for Leave
            }
        },
    },

    # Sexual Orientation
    'sexual-orientation': {
        # Select filter example
        'example': {
            'filter_id': 'sexual-orientation',
            'selected_values': [
                '0',  # heterosexual
                '1',  # homosexual
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'sexual-orientation',
            'selected_values': [
                '0',  # heterosexual
                '1',  # homosexual
            ],
            'weightings': {
                '0': 1,  # Equal weighting for heterosexual
                '1': 1,  # Equal weighting for homosexual
            }
        },
    },

    # Bilingual
    'bilingual': {
        # Select filter example
        'example': {
            'filter_id': 'bilingual',
            'selected_values': [
                '0',  # none just my native langauge
                '1',  # native language + one other language
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'bilingual',
            'selected_values': [
                '0',  # none just my native langauge
                '1',  # native language + one other language
            ],
            'weightings': {
                '0': 1,  # Equal weighting for none just my native langauge
                '1': 1,  # Equal weighting for native language + one other language
            }
        },
    },

    # Body Weight
    'body-weight': {
        # Select filter example
        'example': {
            'filter_id': 'body-weight',
            'selected_values': [
                '0',  # Very Underweight
                '1',  # Underweight
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'body-weight',
            'selected_values': [
                '0',  # Very Underweight
                '1',  # Underweight
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Very Underweight
                '1': 1,  # Equal weighting for Underweight
            }
        },
    },

    # Organizational tenure
    'organizational-tenure': {
        # Select filter example
        'example': {
            'filter_id': 'organizational-tenure',
            'selected_values': [
                '0',  # Less than 2 months
                '1',  # 2-4 months
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'organizational-tenure',
            'selected_values': [
                '0',  # Less than 2 months
                '1',  # 2-4 months
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Less than 2 months
                '1': 1,  # Equal weighting for 2-4 months
            }
        },
    },

    # Country of Birth
    'country-of-birth': {
        # Select filter example
        'example': {
            'filter_id': 'country-of-birth',
            'selected_values': [
                '0',  # United Kingdom
                '1',  # United States
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'country-of-birth',
            'selected_values': [
                '0',  # United Kingdom
                '1',  # United States
            ],
            'weightings': {
                '0': 1,  # Equal weighting for United Kingdom
                '1': 1,  # Equal weighting for United States
            }
        },
    },

    # U.S state/territory of birth
    'us-stateterritory-of-birth': {
        # Select filter example
        'example': {
            'filter_id': 'us-stateterritory-of-birth',
            'selected_values': [
                '0',  # Alabama (AL)
                '1',  # Alaska (AK)
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'us-stateterritory-of-birth',
            'selected_values': [
                '0',  # Alabama (AL)
                '1',  # Alaska (AK)
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Alabama (AL)
                '1': 1,  # Equal weighting for Alaska (AK)
            }
        },
    },

    # Current UK area of residence
    'current-uk-area-of-residence': {
        # Select filter example
        'example': {
            'filter_id': 'current-uk-area-of-residence',
            'selected_values': [
                '0',  # North East, England    (Tees Valley, Durham, Northumberland and Tyne and Wear)
                '1',  # North West, England (Cumbria, Greater Manchester, Lancashire, Merseyside)
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'current-uk-area-of-residence',
            'selected_values': [
                '0',  # North East, England    (Tees Valley, Durham, Northumberland and Tyne and Wear)
                '1',  # North West, England (Cumbria, Greater Manchester, Lancashire, Merseyside)
            ],
            'weightings': {
                '0': 1,  # Equal weighting for North East, England    (Tees Valley, Durham, Northumberland and Tyne and Wear)
                '1': 1,  # Equal weighting for North West, England (Cumbria, Greater Manchester, Lancashire, Merseyside)
            }
        },
    },

    # Vision
    'vision': {
        # Select filter example
        'example': {
            'filter_id': 'vision',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'vision',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Literacy Difficulties
    'literacy-difficulties': {
        # Select filter example
        'example': {
            'filter_id': 'literacy-difficulties',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'literacy-difficulties',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Past Diet
    'past-diet': {
        # Select filter example
        'example': {
            'filter_id': 'past-diet',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'past-diet',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Household Income (GBP)
    'household-income-gbp': {
        # Select filter example
        'example': {
            'filter_id': 'household-income-gbp',
            'selected_values': [
                '0',  # Less than £10,000
                '1',  # £10,000 - £15,999
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'household-income-gbp',
            'selected_values': [
                '0',  # Less than £10,000
                '1',  # £10,000 - £15,999
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Less than £10,000
                '1': 1,  # Equal weighting for £10,000 - £15,999
            }
        },
    },

    # Living with biological child
    'living-with-biological-child': {
        # Select filter example
        'example': {
            'filter_id': 'living-with-biological-child',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'living-with-biological-child',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Evaluating a company's stock as a potential investment
    'evaluating-a-companys-stock-as-a-potential-investment': {
        # Select filter example
        'example': {
            'filter_id': 'evaluating-a-companys-stock-as-a-potential-investment',
            'selected_values': [
                '0',  # Never
                '1',  # Rarely
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'evaluating-a-companys-stock-as-a-potential-investment',
            'selected_values': [
                '0',  # Never
                '1',  # Rarely
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Never
                '1': 1,  # Equal weighting for Rarely
            }
        },
    },

    # Immigration
    'immigration': {
        # Select filter example
        'example': {
            'filter_id': 'immigration',
            'selected_values': [
                '0',  # Yes, I was born in the country I am now living in
                '1',  # No, I moved to the country I am now living in
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'immigration',
            'selected_values': [
                '0',  # Yes, I was born in the country I am now living in
                '1',  # No, I moved to the country I am now living in
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes, I was born in the country I am now living in
                '1': 1,  # Equal weighting for No, I moved to the country I am now living in
            }
        },
    },

    # Romantic Relationship 2
    'romantic-relationship-2': {
        # Select filter example
        'example': {
            'filter_id': 'romantic-relationship-2',
            'selected_values': [
                '0',  # I am in a romantic relationship with someone from the same cultural background as me (ex. Both you and your partner are British)
                '1',  # I am in a romantic relationship with someone from a different cultural background (ex. You are British, but your partner is Russian or American)
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'romantic-relationship-2',
            'selected_values': [
                '0',  # I am in a romantic relationship with someone from the same cultural background as me (ex. Both you and your partner are British)
                '1',  # I am in a romantic relationship with someone from a different cultural background (ex. You are British, but your partner is Russian or American)
            ],
            'weightings': {
                '0': 1,  # Equal weighting for I am in a romantic relationship with someone from the same cultural background as me (ex. Both you and your partner are British)
                '1': 1,  # Equal weighting for I am in a romantic relationship with someone from a different cultural background (ex. You are British, but your partner is Russian or American)
            }
        },
    },

    # Current Country of Residence
    'current-country-of-residence': {
        # Select filter example
        'example': {
            'filter_id': 'current-country-of-residence',
            'selected_values': [
                '0',  # United Kingdom
                '1',  # United States
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'current-country-of-residence',
            'selected_values': [
                '0',  # United Kingdom
                '1',  # United States
            ],
            'weightings': {
                '0': 1,  # Equal weighting for United Kingdom
                '1': 1,  # Equal weighting for United States
            }
        },
    },

    # Religious Affiliation
    'religious-affiliation': {
        # Select filter example
        'example': {
            'filter_id': 'religious-affiliation',
            'selected_values': [
                '0',  # Baha'i
                '1',  # Buddhism
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'religious-affiliation',
            'selected_values': [
                '0',  # Baha'i
                '1',  # Buddhism
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Baha'i
                '1': 1,  # Equal weighting for Buddhism
            }
        },
    },

    # Children
    'children': {
        # Select filter example
        'example': {
            'filter_id': 'children',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'children',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Pain Question
    'pain-question': {
        # Select filter example
        'example': {
            'filter_id': 'pain-question',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'pain-question',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Deception
    'deception': {
        # Select filter example
        'example': {
            'filter_id': 'deception',
            'selected_values': [
                '0',  # Yes, I would be comfortable to take part in such a study
                '1',  # No, I would like to opt-out of any study that uses deception
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'deception',
            'selected_values': [
                '0',  # Yes, I would be comfortable to take part in such a study
                '1',  # No, I would like to opt-out of any study that uses deception
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes, I would be comfortable to take part in such a study
                '1': 1,  # Equal weighting for No, I would like to opt-out of any study that uses deception
            }
        },
    },

    # Mental health/illness/condition - ongoing
    'mental-healthillnesscondition-ongoing': {
        # Select filter example
        'example': {
            'filter_id': 'mental-healthillnesscondition-ongoing',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'mental-healthillnesscondition-ongoing',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Meditation
    'meditation': {
        # Select filter example
        'example': {
            'filter_id': 'meditation',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'meditation',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Internet pornography
    'internet-pornography': {
        # Select filter example
        'example': {
            'filter_id': 'internet-pornography',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'internet-pornography',
            'selected_values': [
                '0',  # Yes
                '1',  # No
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes
                '1': 1,  # Equal weighting for No
            }
        },
    },

    # Internet enabled products
    'internet-enabled-products': {
        # Select filter example
        'example': {
            'filter_id': 'internet-enabled-products',
            'selected_values': [
                '0',  # Smart TV (e.g. Samsung, LG, JVC)
                '1',  # Activity tracker excluding smart watches (e.g. Fitbit, Xiaomi Mi Band, Microsoft band)
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'internet-enabled-products',
            'selected_values': [
                '0',  # Smart TV (e.g. Samsung, LG, JVC)
                '1',  # Activity tracker excluding smart watches (e.g. Fitbit, Xiaomi Mi Band, Microsoft band)
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Smart TV (e.g. Samsung, LG, JVC)
                '1': 1,  # Equal weighting for Activity tracker excluding smart watches (e.g. Fitbit, Xiaomi Mi Band, Microsoft band)
            }
        },
    },

    # Chronic condition/illness
    'chronic-conditionillness': {
        # Select filter example
        'example': {
            'filter_id': 'chronic-conditionillness',
            'selected_values': [
                '0',  # Autoimmune diseases
                '1',  # Cancers
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'chronic-conditionillness',
            'selected_values': [
                '0',  # Autoimmune diseases
                '1',  # Cancers
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Autoimmune diseases
                '1': 1,  # Equal weighting for Cancers
            }
        },
    },

    # Past Employment Sectors
    'past-employment-sectors': {
        # Select filter example
        'example': {
            'filter_id': 'past-employment-sectors',
            'selected_values': [
                '0',  # Agriculture, Food and Natural Resources
                '1',  # Architecture and Construction
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'past-employment-sectors',
            'selected_values': [
                '0',  # Agriculture, Food and Natural Resources
                '1',  # Architecture and Construction
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Agriculture, Food and Natural Resources
                '1': 1,  # Equal weighting for Architecture and Construction
            }
        },
    },

    # Team Sports
    'team-sports': {
        # Select filter example
        'example': {
            'filter_id': 'team-sports',
            'selected_values': [
                '0',  # Archery
                '1',  # Badminton
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'team-sports',
            'selected_values': [
                '0',  # Archery
                '1',  # Badminton
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Archery
                '1': 1,  # Equal weighting for Badminton
            }
        },
    },

    # Pets
    'pets': {
        # Select filter example
        'example': {
            'filter_id': 'pets',
            'selected_values': [
                '0',  # Dog
                '1',  # Cat
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'pets',
            'selected_values': [
                '0',  # Dog
                '1',  # Cat
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Dog
                '1': 1,  # Equal weighting for Cat
            }
        },
    },

    # Online gambling games
    'online-gambling-games': {
        # Select filter example
        'example': {
            'filter_id': 'online-gambling-games',
            'selected_values': [
                '0',  # Baccarat
                '1',  # Blackjack
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'online-gambling-games',
            'selected_values': [
                '0',  # Baccarat
                '1',  # Blackjack
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Baccarat
                '1': 1,  # Equal weighting for Blackjack
            }
        },
    },

    # Consumer review websites
    'consumer-review-websites': {
        # Select filter example
        'example': {
            'filter_id': 'consumer-review-websites',
            'selected_values': [
                '0',  # Amazon
                '1',  # TripAdvisor
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'consumer-review-websites',
            'selected_values': [
                '0',  # Amazon
                '1',  # TripAdvisor
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Amazon
                '1': 1,  # Equal weighting for TripAdvisor
            }
        },
    },

    # Language related disorders
    'language-related-disorders': {
        # Select filter example
        'example': {
            'filter_id': 'language-related-disorders',
            'selected_values': [
                '0',  # reading difficulty
                '1',  # writing difficulty
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'language-related-disorders',
            'selected_values': [
                '0',  # reading difficulty
                '1',  # writing difficulty
            ],
            'weightings': {
                '0': 1,  # Equal weighting for reading difficulty
                '1': 1,  # Equal weighting for writing difficulty
            }
        },
    },

    # Other crowdsourcing platforms select
    'other-crowdsourcing-platforms-select': {
        # Select filter example
        'example': {
            'filter_id': 'other-crowdsourcing-platforms-select',
            'selected_values': [
                '0',  # Amazon's Mechanical Turk
                '1',  # Crowdflower
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'other-crowdsourcing-platforms-select',
            'selected_values': [
                '0',  # Amazon's Mechanical Turk
                '1',  # Crowdflower
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Amazon's Mechanical Turk
                '1': 1,  # Equal weighting for Crowdflower
            }
        },
    },

    # Types of investment
    'types-of-investment': {
        # Select filter example
        'example': {
            'filter_id': 'types-of-investment',
            'selected_values': [
                '0',  # ETF or ETC
                '1',  # Government Bonds
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'types-of-investment',
            'selected_values': [
                '0',  # ETF or ETC
                '1',  # Government Bonds
            ],
            'weightings': {
                '0': 1,  # Equal weighting for ETF or ETC
                '1': 1,  # Equal weighting for Government Bonds
            }
        },
    },

    # Coronary artery disease
    'coronary-artery-disease': {
        # Select filter example
        'example': {
            'filter_id': 'coronary-artery-disease',
            'selected_values': [
                '0',  # Yes, I had a heart attack
                '1',  # Yes, and I had a medical procedure (e.g. stent or bypass surgery)
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'coronary-artery-disease',
            'selected_values': [
                '0',  # Yes, I had a heart attack
                '1',  # Yes, and I had a medical procedure (e.g. stent or bypass surgery)
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes, I had a heart attack
                '1': 1,  # Equal weighting for Yes, and I had a medical procedure (e.g. stent or bypass surgery)
            }
        },
    },

    # Alcohol types
    'alcohol-types': {
        # Select filter example
        'example': {
            'filter_id': 'alcohol-types',
            'selected_values': [
                '0',  # Craft beer
                '1',  # Lager
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'alcohol-types',
            'selected_values': [
                '0',  # Craft beer
                '1',  # Lager
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Craft beer
                '1': 1,  # Equal weighting for Lager
            }
        },
    },

    # Fluent languages
    'fluent-languages': {
        # Select filter example
        'example': {
            'filter_id': 'fluent-languages',
            'selected_values': [
                '0',  # Rather not say
                '1',  # Afrikaans
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'fluent-languages',
            'selected_values': [
                '0',  # Rather not say
                '1',  # Afrikaans
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Rather not say
                '1': 1,  # Equal weighting for Afrikaans
            }
        },
    },

    # Heart Issues
    'heart-issues': {
        # Select filter example
        'example': {
            'filter_id': 'heart-issues',
            'selected_values': [
                '0',  # Yes, and I have an implantable device (e.g. implantable cardiac defibrillator or ventricular assist device)
                '1',  # Yes, and I've had a heart transplant
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'heart-issues',
            'selected_values': [
                '0',  # Yes, and I have an implantable device (e.g. implantable cardiac defibrillator or ventricular assist device)
                '1',  # Yes, and I've had a heart transplant
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Yes, and I have an implantable device (e.g. implantable cardiac defibrillator or ventricular assist device)
                '1': 1,  # Equal weighting for Yes, and I've had a heart transplant
            }
        },
    },

    # Soft drink types
    'soft-drink-types': {
        # Select filter example
        'example': {
            'filter_id': 'soft-drink-types',
            'selected_values': [
                '0',  # Standard carbonated soft drinks (e.g. Fanta; Coca Cola)
                '1',  # Diet/Zero/Low sugar carbonated soft drinks (e.g. Coke Zero; Pepsi Max)
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'soft-drink-types',
            'selected_values': [
                '0',  # Standard carbonated soft drinks (e.g. Fanta; Coca Cola)
                '1',  # Diet/Zero/Low sugar carbonated soft drinks (e.g. Coke Zero; Pepsi Max)
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Standard carbonated soft drinks (e.g. Fanta; Coca Cola)
                '1': 1,  # Equal weighting for Diet/Zero/Low sugar carbonated soft drinks (e.g. Coke Zero; Pepsi Max)
            }
        },
    },

    # Ridesharing services
    'ridesharing-services': {
        # Select filter example
        'example': {
            'filter_id': 'ridesharing-services',
            'selected_values': [
                '0',  # BlaBlaCar
                '1',  # Carma
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'ridesharing-services',
            'selected_values': [
                '0',  # BlaBlaCar
                '1',  # Carma
            ],
            'weightings': {
                '0': 1,  # Equal weighting for BlaBlaCar
                '1': 1,  # Equal weighting for Carma
            }
        },
    },

    # Devices with screens
    'devices-with-screens': {
        # Select filter example
        'example': {
            'filter_id': 'devices-with-screens',
            'selected_values': [
                '0',  # Mobile Phone
                '1',  # Tablet reader
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'devices-with-screens',
            'selected_values': [
                '0',  # Mobile Phone
                '1',  # Tablet reader
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Mobile Phone
                '1': 1,  # Equal weighting for Tablet reader
            }
        },
    },

    # Chat/Messaging apps
    'chatmessaging-apps': {
        # Select filter example
        'example': {
            'filter_id': 'chatmessaging-apps',
            'selected_values': [
                '0',  # Rather not say
                '1',  # Facebook Messenger
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'chatmessaging-apps',
            'selected_values': [
                '0',  # Rather not say
                '1',  # Facebook Messenger
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Rather not say
                '1': 1,  # Equal weighting for Facebook Messenger
            }
        },
    },

    # Experiences at Work
    'experiences-at-work': {
        # Select filter example
        'example': {
            'filter_id': 'experiences-at-work',
            'selected_values': [
                '0',  # I generally feel passionate about my work (that is, excited and highly motivated)
                '1',  # I generally feel respected at work (by my colleagues and/or superiors)
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'experiences-at-work',
            'selected_values': [
                '0',  # I generally feel passionate about my work (that is, excited and highly motivated)
                '1',  # I generally feel respected at work (by my colleagues and/or superiors)
            ],
            'weightings': {
                '0': 1,  # Equal weighting for I generally feel passionate about my work (that is, excited and highly motivated)
                '1': 1,  # Equal weighting for I generally feel respected at work (by my colleagues and/or superiors)
            }
        },
    },

    # Social-Media
    'social-media': {
        # Select filter example
        'example': {
            'filter_id': 'social-media',
            'selected_values': [
                '0',  # Facebook
                '1',  # Youtube
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'social-media',
            'selected_values': [
                '0',  # Facebook
                '1',  # Youtube
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Facebook
                '1': 1,  # Equal weighting for Youtube
            }
        },
    },

    # Hobbies - Categories
    'hobbies-categories': {
        # Select filter example
        'example': {
            'filter_id': 'hobbies-categories',
            'selected_values': [
                '0',  # Art
                '1',  # Economics
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'hobbies-categories',
            'selected_values': [
                '0',  # Art
                '1',  # Economics
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Art
                '1': 1,  # Equal weighting for Economics
            }
        },
    },

    # High School/College/University Sports
    'high-schoolcollegeuniversity-sports': {
        # Select filter example
        'example': {
            'filter_id': 'high-schoolcollegeuniversity-sports',
            'selected_values': [
                '0',  # American football
                '1',  # Badminton
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'high-schoolcollegeuniversity-sports',
            'selected_values': [
                '0',  # American football
                '1',  # Badminton
            ],
            'weightings': {
                '0': 1,  # Equal weighting for American football
                '1': 1,  # Equal weighting for Badminton
            }
        },
    },

    # Credit cards
    'credit-cards': {
        # Select filter example
        'example': {
            'filter_id': 'credit-cards',
            'selected_values': [
                '0',  # Visa
                '1',  # MasterCard
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'credit-cards',
            'selected_values': [
                '0',  # Visa
                '1',  # MasterCard
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Visa
                '1': 1,  # Equal weighting for MasterCard
            }
        },
    },

    # Knowledge of software development techniques 
    'knowledge-of-software-development-techniques': {
        # Select filter example
        'example': {
            'filter_id': 'knowledge-of-software-development-techniques',
            'selected_values': [
                '0',  # Cloud computing
                '1',  # Shell scripting
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'knowledge-of-software-development-techniques',
            'selected_values': [
                '0',  # Cloud computing
                '1',  # Shell scripting
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Cloud computing
                '1': 1,  # Equal weighting for Shell scripting
            }
        },
    },

    # Crime incidents
    'crime-incidents': {
        # Select filter example
        'example': {
            'filter_id': 'crime-incidents',
            'selected_values': [
                '0',  # Theft or attempted theft
                '1',  # Property damage
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'crime-incidents',
            'selected_values': [
                '0',  # Theft or attempted theft
                '1',  # Property damage
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Theft or attempted theft
                '1': 1,  # Equal weighting for Property damage
            }
        },
    },

    # Fashion brand purchases
    'fashion-brand-purchases': {
        # Select filter example
        'example': {
            'filter_id': 'fashion-brand-purchases',
            'selected_values': [
                '0',  # Michael Kors
                '1',  # Louis Vuitton
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'fashion-brand-purchases',
            'selected_values': [
                '0',  # Michael Kors
                '1',  # Louis Vuitton
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Michael Kors
                '1': 1,  # Equal weighting for Louis Vuitton
            }
        },
    },

    # Approval Rate
    'approval_rate': {
        # Range filter example
        'example': {
            'filter_id': 'approval_rate',
            'selected_range': {
                'lower': 0,
                'upper': 100
            }
        },
    },

    # Number of previous submissions
    'approval_numbers': {
        # Range filter example
        'example': {
            'filter_id': 'approval_numbers',
            'selected_range': {
                'lower': 0,
                'upper': 10000
            }
        },
    },

    # Custom Allowlist
    'custom_allowlist': {
        # Select filter example
        'example': {
            'filter_id': 'custom_allowlist',
            'selected_values': [
                '0',  # Add a list of participant ID's you wish to allow to take the study.
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'custom_allowlist',
            'selected_values': [
                '0',  # Add a list of participant ID's you wish to allow to take the study.
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Add a list of participant ID's you wish to allow to take the study.
            }
        },
    },

    # Custom Blocklist
    'custom_blocklist': {
        # Select filter example
        'example': {
            'filter_id': 'custom_blocklist',
            'selected_values': [
                '0',  # Add a list of participant ID's you wish to block from taking the study.
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'custom_blocklist',
            'selected_values': [
                '0',  # Add a list of participant ID's you wish to block from taking the study.
            ],
            'weightings': {
                '0': 1,  # Equal weighting for Add a list of participant ID's you wish to block from taking the study.
            }
        },
    },

    # Joined Between
    'joined_between': {
        # Range filter example
        'example': {
            'filter_id': 'joined_between',
            'selected_range': {
                'lower': '2010-01-01',
                'upper': '2025-04-13'
            }
        },
    },

    # Exclude participants from other studies
    'previous_studies_blocklist': {
        # Select filter example
        'example': {
            'filter_id': 'previous_studies_blocklist',
            'selected_values': [
                '67fb54cd713405244abfeddd',  # My Python-created Study
                '67fb54e99dbd09bdb6121168',  # API Study 1
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'previous_studies_blocklist',
            'selected_values': [
                '67fb54cd713405244abfeddd',  # My Python-created Study
                '67fb54e99dbd09bdb6121168',  # API Study 1
            ],
            'weightings': {
                '67fb54cd713405244abfeddd': 1,  # Equal weighting for My Python-created Study
                '67fb54e99dbd09bdb6121168': 1,  # Equal weighting for API Study 1
            }
        },
    },

    # Include participants from other studies
    'previous_studies_allowlist': {
        # Select filter example
        'example': {
            'filter_id': 'previous_studies_allowlist',
            'selected_values': [
                '67fb54cd713405244abfeddd',  # My Python-created Study
                '67fb54e99dbd09bdb6121168',  # API Study 1
            ]
        },
        # Select filter with weightings example
        'weighted_example': {
            'filter_id': 'previous_studies_allowlist',
            'selected_values': [
                '67fb54cd713405244abfeddd',  # My Python-created Study
                '67fb54e99dbd09bdb6121168',  # API Study 1
            ],
            'weightings': {
                '67fb54cd713405244abfeddd': 1,  # Equal weighting for My Python-created Study
                '67fb54e99dbd09bdb6121168': 1,  # Equal weighting for API Study 1
            }
        },
    },

    # Include participants from a participant group.
    'participant_group_allowlist': {
        # Select filter example
        'example': {
            'filter_id': 'participant_group_allowlist',
            'selected_values': [
            ]
        },
    },

    # Exclude participants from a participant group.
    'participant_group_blocklist': {
        # Select filter example
        'example': {
            'filter_id': 'participant_group_blocklist',
            'selected_values': [
            ]
        },
    },

}

# Example of how to use these filters in a study creation:
'''
study_data = {
    "name": "My Study with Filters",
    ...
    "filters": [
        filter_examples['age']['example'],
        filter_examples['handedness']['example']
    ]
}
'''
