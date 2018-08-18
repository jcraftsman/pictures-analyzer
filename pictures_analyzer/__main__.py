import logging
import os

import click

from pictures_analyzer.analyzer import Analyzer
from pictures_analyzer.http_search_engine import HttpSearchEngine
from pictures_analyzer.local_files_finder import LocalFilesFinder
from pictures_analyzer.s3_safe_box import S3SafeBox
from pictures_analyzer.tesseract_ocr import TesseractOCR


@click.group("analyzer")
@click.option('--debug', default=False, help="Show debug level instructions within analyzer command group",
              is_flag=True)
def main(debug):
    log_level = logging.DEBUG if debug else logging.INFO
    setup_logging(log_level)


@click.command("index")
@click.option("--directory", type=click.Path(exists=True, file_okay=False, resolve_path=True),
              help='The local path to the directory that contains all the pictures to index')
def index(directory):
    get_logger().info('indexing all files in: ', directory)
    search_engine = HttpSearchEngine(os.environ)
    safe_box = S3SafeBox(os.environ)
    finder = LocalFilesFinder()
    optical_character_recognition = TesseractOCR()
    analyzer = Analyzer(search_engine, safe_box, finder, optical_character_recognition)

    analyzer.index(directory)


def setup_logging(log_level):
    logging.basicConfig(
        format="%(asctime)s %(levelname)s - %(message)s [%(filename)s:%(lineno)s] [%(relativeCreated)d]",
        level=log_level)


def get_logger() -> logging.Logger:
    return logging.getLogger('pictures_analyzer')


main.add_command(index)

if __name__ == '__main__':
    main()
