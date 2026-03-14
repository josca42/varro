import os

from prefect.schedules import Cron

from varro.data.statbank_to_disk.prefect_flows import monthly_sync_flow


DEPLOYMENT_NAME = "monthly-statbank-sync"
WORK_POOL = os.getenv("PREFECT_WORK_POOL", "process")
PREFECT_API_URL = os.getenv("PREFECT_API_URL", "http://127.0.0.1:4200/api")
SCHEDULE = Cron("0 22 1 * *", timezone="UTC")
ENTRYPOINT = "varro/data/statbank_to_disk/prefect_flows.py:monthly_sync_flow"


def deploy_monthly_sync() -> None:
    os.environ["PREFECT_API_URL"] = PREFECT_API_URL
    monthly_sync_flow.from_source(source=".", entrypoint=ENTRYPOINT).deploy(
        name=DEPLOYMENT_NAME,
        work_pool_name=WORK_POOL,
        schedules=[SCHEDULE],
        parameters={"max_tables": None},
        build=False,
        push=False,
        print_next_steps=False,
    )


if __name__ == "__main__":
    deploy_monthly_sync()
