import sys
import oci
from oci.config import from_file
from oci.config import validate_config

config = from_file()

validate_config(config)

# get config
compartment_id = config["tenancy"]
MY_ADB_ID = "ocid1.autonomousdatabase.oc1.eu-frankfurt-1.abtheljtwnrioduazul6zqhqrtmqs725m2jkjnyn5u6fzqrwrq3wowsbdzia"

#
# funzione che fa update config DB
#
def update_adb(db_client, adb_id, n_ocpu, auto_scale):
    adb_request = oci.database.models.UpdateAutonomousDatabaseDetails()

    adb_request.cpu_core_count = n_ocpu
    adb_request.is_auto_scaling_enabled = auto_scale

    adb_response = db_client.update_autonomous_database(adb_id,
                                                        update_autonomous_database_details=adb_request,
                                                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY)

    print("ADB updated....")

    return adb_response.data.id

#
# main section
#

# legge argomenti da command line
if len(sys.argv) < 3:
   print("Missing command line params...")
   print("Usage: python3 scala_atp.py N_CORE AUTO_SCALE.")
   sys.exit(-1)
else:
   n_ocpu = int(sys.argv[1])
   if sys.argv[2] == "True":
       auto_scaling = True
   else:
       auto_scaling = False

   print("Executing with params: %s %s" %(n_ocpu, auto_scaling))

print("Scaling up ATP...")

db_client = oci.database.DatabaseClient(config)

update_adb(db_client, MY_ADB_ID, n_ocpu, auto_scaling)

