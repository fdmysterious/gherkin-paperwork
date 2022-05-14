# This is comment line
@my_feature_tag
Feature: Alarm

	This feature checks that an alarm can wether work or
	not.

	@my_scenario_tag
	Scenario: Waking is good

		Tests the nominal case

		Given Florian is asleep
		When the alarm rings
		Then Florian wakes up
		And Florian shuts the alarm down

	Scenario: Waking is bad

		Tests the error case

		Given Florian is asleep
		When the alarm rings
		And Florian stays asleep
		When 10m are spent
		Then the Alarm stops

	Scenario: Waking is complex

		Tests some special cases

		Given Florian is asleep
		And the day is one of the following:
			| Saturday |
			| Sunday   |

		Then Florian doesn't want to wake up
