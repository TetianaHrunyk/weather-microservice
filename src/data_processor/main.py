import logging
import click
from time import sleep

from src.data_processor.helpers import get_data, insert_data


logger = logging.getLogger(__name__)


@click.command()
@click.option(
    "--frequency_sec", default=60 * 60 * 60, help="How often to sync the temperature"
)
def main(frequency_sec):
    logger.info(f"Start data processor with frequency {frequency_sec}")
    while True:
        data = get_data()
        insert_data(data)
        logger.info(f"Inserted record {data}")
        sleep(frequency_sec)


if __name__ == "__main__":
    main()
