import os

from prefect.schedules import Cron

from varro.data.statbank_to_disk.prefect_flows import weekly_statbank_sync_flow


DEPLOYMENT_NAME = "weekly-statbank-sync"
WORK_POOL = os.getenv("PREFECT_WORK_POOL", "process")
SCHEDULE = Cron("0 22 * * 0", timezone="UTC")


def deploy_weekly_sync() -> None:
    weekly_statbank_sync_flow.deploy(
        name=DEPLOYMENT_NAME,
        work_pool_name=WORK_POOL,
        schedules=[SCHEDULE],
        parameters={"force_catalog_poll": False},
        build=False,
        push=False,
        print_next_steps=False,
    )


if __name__ == "__main__":
    deploy_weekly_sync()
