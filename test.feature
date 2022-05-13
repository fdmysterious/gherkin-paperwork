# This is comment line
@my_feature_tag
Feature: Alarm
	# Hello world!
	@my_scenario_tag
	Scenario: Waking is good
		Given Florian is asleep
		When the alarm rings
		Then Florian wakes up
		And Florian shuts the alarm down

	Scenario: Waking is bad
		Given Florian is asleep
		When the alarm rings
		And Florian stays asleep
		When 10m are spent
		Then the Alarm stops

	Scenario: Waking is complex
		Given Florian is asleep
		And the day is one of the following:
			| Saturday |
			| Sunday   |

		Then Florian doesn't want to wake up
