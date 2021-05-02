from apps.site_monitor.monitor import SiteMonitor
mon = SiteMonitor()


def test_valid_response_from_monitor():
    mon.base_url = 'https://docs.pytest.org'
    data = mon.get_stats()
    assert list(data.keys()) == ["data"]


def test_gracefully_fail_on_exception():
    mon.base_url = 'not-a-urls'
    data = mon.get_stats()
    assert data is None
