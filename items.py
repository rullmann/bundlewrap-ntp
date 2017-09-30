pkg_dnf = {
    'ntp': {},
    'ntpdate': {},
    'chrony': {
        'installed': False,
    },
}

svc_systemd = {
    'ntpd': {
        'needs': [
            'pkg_dnf:ntp',
        ],
    },
}

files = {
    '/etc/ntp.conf': {
        'source': 'ntp.conf',
        'needs': [
            'pkg_dnf:ntp',
        ],
        'triggers': [
            'svc_systemd:ntpd:restart',
        ],
    },
}

if node.has_bundle('collectd'):
    files['/etc/collectd.d/ntp.conf'] = {
        'source': 'collectd_ntp.conf',
        'mode': '0640',
        'needs': [
            'pkg_dnf:ntp',
        ],
        'triggers': [
            'svc_systemd:collectd:restart',
        ],
    }
