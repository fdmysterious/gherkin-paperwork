Feature: Alarm
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
