pkt_yum = {
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
