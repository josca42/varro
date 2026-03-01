import os

from prefect.schedules import Cron

from varro.data.statbank_to_disk.prefect_flows import weekly_statbank_sync_flow


DEPLOYMENT_NAME = "weekly-statbank-sync"
WORK_POOL = os.getenv("PREFECT_WORK_POOL", "process")
PREFECT_API_URL = os.getenv("PREFECT_API_URL", "http://127.0.0.1:4200/api")
SCHEDULE = Cron("0 22 * * 0", timezone="UTC")
ENTRYPOINT = "varro/data/statbank_to_disk/prefect_flows.py:weekly_statbank_sync_flow"


def deploy_weekly_sync() -> None:
    os.environ["PREFECT_API_URL"] = PREFECT_API_URL
    weekly_statbank_sync_flow.from_source(source=".", entrypoint=ENTRYPOINT).deploy(
        name=DEPLOYMENT_NAME,
        work_pool_name=WORK_POOL,
        schedules=[SCHEDULE],
        parameters={"force_catalog_poll": False, "max_tables": None},
        build=False,
        push=False,
        print_next_steps=False,
    )


if __name__ == "__main__":
    deploy_weekly_sync()
