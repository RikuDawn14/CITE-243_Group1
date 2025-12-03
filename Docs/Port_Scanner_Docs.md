# Port Scanner Module

## Description
A multi-threaded network port scanner with a graphical interface that identifies open ports and running services on target hosts. Built as a modular component for the NIC CITE 243 Group Project.

## What It Does
- Scans IP addresses or domain names for open network ports
- Identifies common services running on open ports (SSH, HTTP, MySQL, etc.)
- Displays real-time scan progress with a visual progress bar
- Exports detailed scan results to JSON format with timestamps
- Supports configurable port ranges (1-65535) and scanning parameters

## How It Works
The scanner uses Python's `socket` library to attempt TCP connections on specified ports. Multi-threading via `ThreadPoolExecutor` enables concurrent scanning of multiple ports, significantly improving scan speed. The Qt framework provides a non-blocking GUI that remains responsive during scans by running the scan operation in a separate worker thread using `QThread`.

When a port responds, the scanner checks it against a dictionary of common services to identify what's running. All results are collected and can be exported as structured JSON data for documentation or further analysis.

## Technologies Used
- **Python 3.x** - Core programming language
- **PySide6 (Qt)** - GUI framework and threading
- **socket** - Network port connection testing
- **concurrent.futures** - Multi-threaded port scanning
- **json** - Data export functionality
- **datetime** - Timestamp generation

## Features
- Configurable thread count (1-500 concurrent scans)
- Adjustable connection timeout
- Start/Stop scan controls
- Service detection for 25+ common ports
- Color-coded results display
- JSON export with full scan metadata
