Repository con il codice per l'esempio di scalabilità ed automazione **Oracle Autonomous DB**

utilizzato nel **workshop OCI** del 14/05/2020

L.S. 13/05/2020

1. Per il setup di Swingbench, suggerisco il blog di D. Gilles (autore di Swingbench)

	http://www.dominicgiles.com/blog/files/c84a63640d52961fc28f750570888cdc-169.html

	La soluzione più semplice ed efficace è di creare una VM in OCI ed usarla per simulare l'AS. In tale VM si fa girare Swingbench (run1.sh). 
	Per test si può lanciare anche da una macchina remota (non i n OCI), ma in questo caso la  velocità della connessione può influenzare i risultati.

	La versione di Swingbench che io ho usato durante la demo è la 2.6.

	Lo schema dati usato è SOE, che simula un sistema di Order Entry.

2. Per il run della simulazione uso lo script run1.sh, da collocare in swingbench/bin

3. Per cambiare la configurazione CPU di ATP uso: scala_atp.py

4. La documentazione del OCI Python SDK è disponibile alla URL:

	https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/

5. Per configurare l'accesso ad OCI da SDK:

	https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm



