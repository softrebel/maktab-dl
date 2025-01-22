import click
import os
from maktab_dl.handler import MaktabkhoonehCrawler
from maktab_dl.utils import (
    get_cookies_default_file_path,
    get_user_default_path,
    get_boolean_manual,
)


@click.group()
def cli():
    """
    A simple command-line interface for interacting with Maktabkhooneh.
    """
    pass


@cli.command()
@click.option(
    "--url",
    required=True,
    type=str,
    help="Course url in Maktabkhooneh",
)
@click.option(
    "--cookies",
    required=False,
    type=str,
    default=get_cookies_default_file_path(),
    help="Path to the cookies file",
)
@click.option(
    "--output",
    required=False,
    type=str,
    default=get_user_default_path(),
    help="Path to the output directory",
)
def download(url: str, cookies: str, output: str):
    """Loads course information from a url and downloads videos for that course."""
    try:
        if not os.path.exists(cookies):
            click.echo(
                "Cookies file not found. You must Enter Maktabkhooneh Username and Password."
            )
            username = click.prompt("Enter Username", type=str)
            password = click.prompt("Enter Password", hide_input=True, type=str)
            crawler = MaktabkhoonehCrawler(
                username=username,
                password=password,
                cookies_path=cookies,
                output_path=output,
            )

            force_save_cookies = get_boolean_manual(
                f"If you want to save cookies on the path `{cookies}` you selected?"
            )
            crawler.login(force_save_cookies=force_save_cookies)
        else:
            crawler = MaktabkhoonehCrawler(
                cookies_path=cookies,
                output_path=output,
            )
            crawler.init_cookies()
            if len(crawler.client.cookies.jar) == 0:
                click.echo("No Cookies. Please login first.")
                return

        course_info = crawler.crawl_course_link(input_link=url)
        cleaned_link = course_info.link
        crawler.enroll_course_link(cleaned_link)
        crawler.download_course_videos(course_info)
        click.echo(f"Finished downloading course videos from: {cleaned_link}")
    except Exception as e:
        click.echo(f"Error downloading videos: {e}")


if __name__ == "__main__":
    cli()
