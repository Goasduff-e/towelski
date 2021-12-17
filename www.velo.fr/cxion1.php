<h2 align="center">
<?php 

$loginOK =false;

	// On vérifie que l'utilisateur et son mots de passe sont corrects
	if (($_POST['login']) == 'stiv')
	{
		if (($_POST['password']) == '1234')
		{$loginOK = true;
		}
	}
// Si le login a été validé on agit
if ($loginOK)
	{ echo ' Ton identifiant est : '.$_POST['login'];

	?>
	<h2 align="center">
	<?php 

	echo 'Ton mot de passe est : '.$_POST['password'];
	?>
	<form action="pagesecrete.html" method="post1">
	<h1> <input style="width: 30%" align="center" type= "submit" value="Votre compte"></h1>
	</form>
<?php	
	}

else
	{ echo ' Une erreur est survenue. Veuillez réessayer !';
	?>
	<form action="Connexion.html" method="post1">
	<h1> <input style="width: 30%" align="center" type= "submit" value="Revenez en arrière"></h1>
	</form>
	<?php
	}
?>
