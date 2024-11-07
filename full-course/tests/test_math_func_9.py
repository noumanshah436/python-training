import pytest
from unittest import mock


# Sample Project class
class Project:
    def __init__(self, _id, domains):
        self._id = _id
        self.domains = domains

    @classmethod
    async def find_by_domains(cls, domains):
        if "example.com" in domains:
            return Project(_id="project_123", domains=["example.com"])
        return None

    @classmethod
    async def find_by_id(cls, _id):
        if _id == "project_123":
            return Project(_id="project_123", domains=["example.com"])
        return None


# A simplified function to associate emails with a project
async def associate_email_with_project(email, org_id):
    project = await Project.find_by_domains([email["from"]])
    if project:
        return {"project": project, "email": email}
    return None


# Simplified mock test
@pytest.mark.asyncio
@mock.patch.object(
    Project, "find_by_domains", new_callable=mock.AsyncMock
)
@mock.patch.object(
    Project, "find_by_id", new_callable=mock.AsyncMock
)
async def test_associate_email_with_project(mock_find_by_domains, mock_find_by_id):
    """
    Test that the email is associated with the project if the email is from 'example.com'.
    """

    # Sample email to associate with the project
    email = {
        "id": "email_1",
        "from": "someone@example.com",
        "to": ["user1@domain.com"],
        "subject": "Test Email",
        "body": "Test body content"
    }

    # Mock behavior for find_by_domains
    mock_find_by_domains.return_value = Project(
        _id="project_123", domains=["example.com"])
    mock_find_by_id.return_value = Project(
        _id="project_123", domains=["example.com"])

    # Call the function to associate the email with a project
    result = await associate_email_with_project(email, "org_123")

    # Assertions
    assert result is not None
    assert result["project"]._id == "project_123"  # The project is returned
    assert result["project"].domains == [
        "example.com"]  # The project domain matches
    # The email is correct
    assert result["email"]["from"] == "someone@example.com"

    # Ensure the mock method was called as expected
    # mock_find_by_domains.assert_called_once_with(["someone@example.com"])
    # mock_find_by_id.assert_called_once_with("project_123")


# **************************************8

# pytest test_math_func_9.py -v