pkg_yum = {
    "ntp": {},
    "ntpdate": {},
}

svc_systemd = {
    'ntpd': {
        'enabled': True,
        'needs': [
            "pkg_yum:ntp",
        ],
    },
}

files = {
    "/etc/ntp.conf": {
        "source": "ntp.conf",
        'needs': [
            "pkg_yum:ntp",
        ],
        'triggers': [
            "svc_systemd:ntpd:restart",
        ],
    },
}

if node.has_bundle("collectd"):
    files['/etc/collectd.d/ntp.conf'] = {
        'source': "collectd_ntp.conf",
        'mode': "0640",
        'owner': "root",
        'group': "root",
        'needs': [
            "pkg_yum:ntp",
        ],
        'triggers': [
            "svc_systemd:collectd:restart",
        ],
    }