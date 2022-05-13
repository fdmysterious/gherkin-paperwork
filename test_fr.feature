# language: fr
Fonctionnalité: Réveil matin
	Scenario: Le réveil qui se passe bien
		Etant donné que Florian soit endormi
		Lorsque le réveille sonne
		Alors Florian se réveille
		Et éteint le réveil

	Scenario: Le réveil qui ne se passe pas bien
		Etant donné que Florian soit endormi
		Lorsque le réveille sonne
		Et Florian ne se réveille pas
		Alors le réveil continue de sonner
		Lorsque 10min se sont écoulées
		Alors le réveil s'éteint
