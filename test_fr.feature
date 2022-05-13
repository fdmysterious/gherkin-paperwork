# language: fr
Fonctionnalité: Réveil matin

	Cette fonctionnalité vérifie si un réveil matin
	peut fonctionner ou non.

	Scénario: Le réveil qui se passe bien
		Etant donné que Florian soit endormi
		Lorsque le réveille sonne
		Alors Florian se réveille
		Et éteint le réveil

	Scénario: Le réveil qui ne se passe pas bien
		Etant donné que Florian soit endormi
		Lorsque le réveille sonne
		Et Florian ne se réveille pas
		Alors le réveil continue de sonner
		Lorsque 10min se sont écoulées
		Alors le réveil s'éteint

	Scénario: Le réveil est compliqué
		Etant donné que Florian soit endormi
		Lorsque nous sommes à un des jours suivants :
			| Samedi   |
			| Dimanche |

		Alors Florian ne veut pas se réveiller.
