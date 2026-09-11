"""
Security layer for Warehouse Ops MCP Toolkit.

The current site is derived from authenticated user context.
For this assessment we simulate the authenticated user's site.
"""


CURRENT_USER_SITE = "LEEDS-01"


def get_current_site() -> str:
    """
    Return the current authenticated user's site.
    """
    return CURRENT_USER_SITE


def has_site_access(site: str) -> bool:
    """
    Check whether the current user can access the requested site.
    """

    return site == CURRENT_USER_SITE


def access_denied_response(site: str) -> dict:
    """
    Standard access denied response.
    """

    return {
        "success": False,
        "error_code": "ACCESS_DENIED",
        "message": (
            f"Access to site '{site}' is not permitted."
        ),
        "current_site": CURRENT_USER_SITE
    }