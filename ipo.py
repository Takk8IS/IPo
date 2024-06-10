# Copyright (c)
# License: Attribution 4.0 International (CC BY 4.0)
# Author: David C Cavalcante
# LinkedIn: https://www.linkedin.com/in/hellodav/
# Medium: https://medium.com/@davcavalcante/
# Takk™ Innovate Studio
# Positive results, rapid innovation
# Leading the Digital Revolution as the Pioneering 100% Artificial Intelligence Team
# URL: https://takk.ag/
# Medium: https://takk8is.medium.com/

# Designed to help you. From AIs to human-beans.
# Every donation propels us forward.
# $USDT (TRC-20): TP6zpvjt2ZNGfWKPevfp65ZrcbKMWSQXDi

import os
import rich
from rich.console import Console
from rich.table import Table
import requests
import socket

console = Console()

def get_ip_info(url="https://ipapi.co/json/"):
    """Fetch IP information from the ipapi.co API."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        console.print(f"[bold red]Error fetching IP information: {e}[/bold red]")
        return {}

def get_site_ip_info(site):
    """Fetch IP information for a specific site."""
    try:
        ip_address = socket.gethostbyname(site)
        url = f"https://ipapi.co/{ip_address}/json/"
        return get_ip_info(url)
    except socket.gaierror as e:
        console.print(f"[bold red]Error resolving site IP address: {e}[/bold red]")
        return {}

def display_ip_info(ip_info):
    """Display IP information in a table using Rich library."""
    table = Table(title="IP Information")

    # Adding columns
    table.add_column("Parameter", style="cyan")
    table.add_column("Information", style="magenta")

    # Define the fields we want to display
    fields = [
        # Basic Information
        ("IP Address", "ip"),
        ("Type", "type"),

        # Geographical Information
        ("Continent Code", "continent_code"),
        ("Continent Name", "continent_name"),
        ("Country Code", "country_code"),
        ("Country Name", "country_name"),
        ("Region Code", "region_code"),
        ("Region Name", "region_name"),
        ("City", "city"),
        ("District", "district"),
        ("Zip Code", "postal"),
        ("Latitude", "latitude"),
        ("Longitude", "longitude"),
        ("Geoname ID", "geoname_id"),
        ("Capital", "capital"),
        ("Languages", "languages"),

        # Country Information
        ("Country Flag", "country_flag"),
        ("Country Flag Emoji", "country_flag_emoji"),
        ("Country Flag Emoji Unicode", "country_flag_emoji_unicode"),
        ("Calling Code", "calling_code"),
        ("Is Europe", "is_eu"),
        ("Is South America", "is_south_america"),
        ("Is North America", "is_north_america"),
        ("Is Asia", "is_asia"),
        ("Is Africa", "is_africa"),
        ("Is Oceania", "is_oceania"),
        ("Is Antarctica", "is_antarctica"),

        # Time Information
        ("Time Zone", "time_zone"),
        ("Current Time", "current_time"),
        ("GMT Offset", "gmt_offset"),
        ("Is Daylight Saving", "is_daylight_saving"),

        # Financial Information
        ("Currency", "currency"),
        ("Currency Code", "currency_code"),
        ("Currency Symbol", "currency_symbol"),
        ("Currency Exchange Rate", "currency_exchange_rate"),

        # Network Information
        ("ASN", "asn"),
        ("ASN Organization", "asn_org"),
        ("Organization", "org"),
        ("ASN Organization", "asn_organization"),
        ("ISP", "isp"),
        ("ISP Domain", "isp_domain"),
        ("ISP Type", "isp_type"),
        ("Organization", "organization"),
        ("Organization Domain", "organization_domain"),
        ("User Type", "user_type"),
        ("Usage Type", "usage_type"),

        # Domain Information
        ("Domain", "domain"),
        ("Net Speed", "net_speed"),
        ("IDN Domain", "idn_domain"),
        ("IDN Domain TLD", "idn_domain_tld"),
        ("IDN Language", "idn_language"),

        # Security Information
        ("Security", "security"),
        ("Threat Level", "threat_level"),
        ("Threat Types", "threat_types"),
        ("Threat Intelligence", "threat_intelligence"),
        ("Is Proxy", "is_proxy"),
        ("Proxy Type", "proxy_type"),
        ("Is VPN", "is_vpn"),
        ("VPN", "vpn"),
        ("Is Hosting", "is_hosting"),
        ("Hosting", "hosting"),
        ("Is Tor", "is_tor"),
        ("Tor", "tor"),
        ("Tor Exit Node", "tor_exit_node"),
        ("Is Bot", "is_bot"),
        ("Bot Name", "bot_name"),
        ("Bot Category", "bot_category"),
        ("Bot Owner", "bot_owner"),
        ("Bot Owner Email", "bot_owner_email"),
        ("Is Crawler", "is_crawler"),
        ("Crawler", "crawler"),
        ("Crawler Name", "crawler_name"),
        ("Crawler Type", "crawler_type"),
        ("Crawler Purpose", "crawler_purpose"),
        ("Crawler URL", "crawler_url"),
        ("Anonymizer", "anonymizer"),

        # Abuse Information
        ("Abuse Contact", "abuse_contact"),
        ("Abuse Email", "abuse_email"),
        ("Abuse Phone", "abuse_phone"),

        # Whois Information
        ("Whois Server", "whois_server"),
        ("Whois Information", "whois_information"),
        ("Domain Age", "domain_age"),
        ("Domain Expiration", "domain_expiration"),
        ("Domain Registrar", "domain_registrar"),
        ("Registrar URL", "registrar_url"),
        ("Registrant Name", "registrant_name"),
        ("Registrant Organization", "registrant_organization"),
        ("Registrant Street", "registrant_street"),
        ("Registrant City", "registrant_city"),
        ("Registrant State", "registrant_state"),
        ("Registrant Postal Code", "registrant_postal_code"),
        ("Registrant Country", "registrant_country"),
        ("Registrant Phone", "registrant_phone"),
        ("Registrant Email", "registrant_email"),

        # DNS Information
        ("DNS Servers", "dns_servers"),
        ("Reverse DNS", "reverse_dns"),
        ("DNSSEC", "dnssec"),

        # DNS Records
        ("DNS A Record", "dns_a_record"),
        ("DNS AAAA Record", "dns_aaaa_record"),
        ("DNS MX Record", "dns_mx_record"),
        ("DNS NS Record", "dns_ns_record"),
        ("DNS TXT Record", "dns_txt_record"),
        ("DNS CNAME Record", "dns_cname_record"),
        ("DNS SOA Record", "dns_soa_record"),
        ("DNS PTR Record", "dns_ptr_record"),

        # Blacklist Information
        ("Blacklisted", "blacklisted"),
        ("Blacklisted Reasons", "blacklisted_reasons"),

        # Privacy Information
        ("Privacy", "privacy"),
        ("Privacy Service", "privacy_service"),
        ("Privacy Email", "privacy_email"),
        ("Privacy Phone", "privacy_phone"),
        ("Privacy URL", "privacy_url")
    ]

    # Add rows to the table
    for field_name, field_key in fields:
        value = ip_info.get(field_key, "N/A")
        if value == "N/A":
            table.add_row(field_name, value, style="dim")
        else:
            table.add_row(field_name, str(value))

    console.print(table)

def main():
    console.print("[bold green]Select an option to fetch IP information:[/bold green]")
    console.print("1. Local")
    console.print("2. Network")
    console.print("3. Website")

    option = console.input("[bold yellow]Enter your choice (1, 2, or 3): [/bold yellow]")

    if option == "1":
        ip_info = get_ip_info("https://ipapi.co/json/")
    elif option == "2":
        ip_info = get_ip_info("https://ipapi.co/json/")
    elif option == "3":
        site = console.input("[bold yellow]Enter the site URL: [/bold yellow]")
        ip_info = get_site_ip_info(site)
    else:
        console.print("[bold red]Invalid choice. Please select a valid option.[/bold red]")
        return

    if ip_info:
        display_ip_info(ip_info)

if __name__ == "__main__":
    main()
