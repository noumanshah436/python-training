import requests
from bs4 import BeautifulSoup

class WebScraper:
  # make it constant
  url = "https://realpython.github.io/fake-jobs/"

  def __init__(self):
    page = requests.get(WebScraper.url)
    self.soup = BeautifulSoup(page.content, 'html.parser')
    self.jobs = []


  def get_all_jobs(self):
    results = self.soup.find(id="ResultsContainer")
    job_elements = results.find_all("div", class_="card-content")

    for job_element in job_elements:
      title_element = job_element.find("h2", class_="title")
      company_element = job_element.find("h3", class_="company")
      location_element = job_element.find("p", class_="location")

# We can create a serializer/decorator or a child class whatever feels better
      job = {
        "job_title": title_element.text.strip(),
        "job_company": company_element.text.strip(),
        "job_location": location_element.text.strip(),
      }

      self.jobs.append(job)

    return self.jobs


  def get_jobs_by_title(self, job_title):
    results = self.soup.find(id="ResultsContainer")
    jobs_by_title = results.find_all(
      "h2", string=lambda text: job_title in text.lower()
    )

    for job_element in jobs_by_title:
      job = job_element.parent.parent.parent
      title_element = job.find("h2", class_="title")
      company_element = job.find("h3", class_="company")
      location_element = job.find("p", class_="location")

      job = {
        "job_title": title_element.text.strip(),
        "job_company": company_element.text.strip(),
        "job_location": location_element.text.strip(),
      }

      self.jobs.append(job)

    return self.jobs


  def store_jobs_in_file(self, title):
    if not self.jobs:
        print("Jobs not available")
        return

    try:
        with open("jobs.txt", "w+") as file:
          file.write(f"**** {title} ****\n\n")
          for job in self.jobs:
            file.write(WebScraper.make_job_string(job))

          file.seek(0,0)
          print(f"\n\n{file.read()}")

    except IOError as e:
        print(f"An error occurred while writing to 'jobs.txt': {e}")


  @staticmethod
  def make_job_string(job):
    job_title = job.get('job_title', 'N/A')
    job_company = job.get('job_company', 'N/A')
    job_location = job.get('job_location', 'N/A')

    return f"Job Title: {job_title}\nCompany: {job_company}\nLocation: {job_location}\n\n"



def main():
    try:
        scraper = WebScraper()

        print("""Options:
        1. Get All Jobs
        2. Search job by title
        """)

        option = int(input("Enter option: "))

        if option == 1:
            scraper.get_all_jobs()
            scraper.store_jobs_in_file("All Jobs")
        elif option == 2:
            job_title = input("Enter job title: ")
            scraper.get_jobs_by_title(job_title.lower())
            scraper.store_jobs_in_file(f"All {job_title.capitalize()} Jobs")
        else:
            print("Enter Valid Option")

    except ValueError:
        print("Invalid input. Please enter a valid option as an integer.")
    except FileNotFoundError:
        print("The 'jobs.txt' file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


main()

