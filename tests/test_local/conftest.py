import os
from dapodik_webservice import DapodikWebservice
from dotenv import load_dotenv
from pytest import fixture

load_dotenv()


DAPODIK_TOKEN = os.getenv("DAPODIK_TOKEN", "")
NPSN = os.getenv("NPSN", "")


@fixture
def dapodik() -> DapodikWebservice:
    return DapodikWebservice(DAPODIK_TOKEN, NPSN)
