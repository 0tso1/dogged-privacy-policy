+++
title = 'Privacy Policy'
date = 2025-11-13
+++

# Privacy Policy for Dogged: Raw Dogging Practise

**Last Updated:** November 13, 2025

**App Name:** Dogged: Raw Dogging Practise
**Package Name:** com.rawdog.app
**Developer:** Dogged App Team

## Introduction

Welcome to Dogged: Raw Dogging Practise ("Dogged," "we," "us," or "our"). We are committed to protecting your privacy and being transparent about the data we collect and how we use it.

This Privacy Policy explains what information we collect when you use our mobile application and how that information is used, stored, and protected.

## Information We Collect

### Data We Collect and Store Online

When you use Dogged, we collect and store the following information in our online database (powered by Cloudflare D1 SQL database via Cloudflare Workers):

- **Username**: Your chosen username when you first open the app. This is used to identify you on the global leaderboard.
- **Score**: Your score achieved in the app sessions, used for leaderboard rankings.
- **Device ID**: A unique identifier for your device, used to prevent duplicate usernames and ensure fair play. This is either:
  - Android: Your Android ID
  - iOS: Your iOS Identifier for Vendor
  - Or a randomly generated UUID if neither is available

  This device ID is stored locally on your device and sent to our server only when submitting scores.
- **Timestamp**: The date and time when scores are submitted.

### Data Processed Locally (Never Leaves Your Device)

- **Face Detection Data**: All face detection and head pose tracking occurs entirely on your device using on-device ML Kit (Google Mobile Vision). The app uses your front-facing camera to detect when you're looking at the screen, but:
  - **No images or video are ever transmitted** from your device
  - **No facial recognition data is stored** on our servers
  - **No biometric data leaves your device**
  - Processing uses hardware-accelerated machine learning models that run locally
  - The app only tracks head orientation angles (yaw and pitch within ±10 degrees) to determine if you're looking at the screen

### Camera Permission

The app requests camera permission with the following message:
> "This app needs camera access to detect your face and track eye contact time."

Camera access is used **exclusively** for local face detection. No camera data is transmitted or stored remotely.

### Data We Do NOT Collect

We do not collect:
- Personal identification information (email, phone number, real name, address)
- Payment information (the app is free)
- Location data or GPS coordinates
- Contacts, photos, or other media from your device
- Device information beyond the device ID (no hardware specs, model, etc.)
- Usage analytics or tracking data
- Any biometric data, facial images, or camera footage
- Browsing history or other app usage

## How We Use Your Information

We use the collected information solely for the following purposes:

- **Username**: To identify you on the global leaderboard and display your ranking
- **Score**: To calculate and display your ranking on the global leaderboard
- **Device ID**: To prevent duplicate usernames, ensure one username per device, and maintain fair competition
- **Timestamp**: To track when scores were achieved and maintain leaderboard freshness

## Data Storage and Security

### Online Database
- Your username, scores, device ID, and timestamps are stored in a Cloudflare D1 SQL database
- The database is accessed via Cloudflare Workers API endpoint: `https://raw-dog-api.otso-tolonen.workers.dev`
- Cloudflare implements industry-standard security measures to protect data
- All data transmissions use secure HTTPS/TLS encryption
- The database is hosted on Cloudflare's global network with built-in DDoS protection

### Local Processing
- All face detection processing happens locally on your device using ML Kit (Google Mobile Vision)
- Face detection uses hardware-accelerated on-device machine learning models
- No facial data, images, or video frames are transmitted over the internet
- No facial or biometric data is stored on our servers
- Camera data is processed in real-time and immediately discarded

### Data Retention
- Leaderboard data is retained indefinitely to maintain historical rankings
- Local device data (username, device ID) is stored on your device using AsyncStorage
- You can request deletion of your data at any time (see "Your Rights and Choices" below)

## Data Sharing and Third Parties

We do **not** sell, trade, or share your personal information with third parties, except:

- **Cloudflare**: Acts as our infrastructure provider for:
  - Database hosting (Cloudflare D1)
  - API hosting (Cloudflare Workers)
  - Network security and DDoS protection
- **Google (ML Kit)**: Face detection runs entirely on-device using Google's ML Kit framework. No data is sent to Google servers during face detection.
- **Legal Requirements**: We may disclose information if required by law, court order, or to protect our legal rights

## Your Rights and Choices

You have the right to:

- **Access Your Data**: Request a copy of your username, scores, device ID, and timestamps stored in our database
- **Delete Your Data**: Request deletion of your username, scores, and associated data from our database
- **Update Your Data**: While the app allows you to set your username once per device, you can contact us to update or change it
- **Camera Permissions**: You can revoke camera permissions at any time through your device settings. Note that the app requires camera access to function.

To exercise these rights, please contact us at the email address provided below. We will respond to your request within 30 days.

### How to Control Your Data

- **Camera Access**: Manage in your device's Settings > Apps > Dogged > Permissions
- **Local Data**: Clear by uninstalling the app (this removes locally stored username and device ID)
- **Server Data**: Contact us to request deletion from the leaderboard database

## Children's Privacy

Dogged is intended for users aged 13 and older. We do not knowingly collect personal information from children under 13 years of age without parental consent.

If you are under 13 years old, please do not use this app or provide any personal information without your parent or guardian's permission.

If you are a parent or guardian and believe your child under 13 has provided us with personal information without your consent, please contact us immediately and we will take steps to remove that information from our systems.

## Changes to This Privacy Policy

We may update this Privacy Policy from time to time to reflect changes in our practices, technology, legal requirements, or other factors. Any changes will be posted on this page with an updated "Last Updated" date at the top.

We encourage you to review this policy periodically. Your continued use of the app after changes are posted constitutes acceptance of the updated policy.

## International Users

By using Dogged, you consent to the transfer and processing of your data in accordance with this Privacy Policy, regardless of your country of residence. The data is stored on Cloudflare's global network, which may involve transfer to countries outside your own.

Cloudflare maintains compliance with international data protection regulations including GDPR and CCPA.

## Technical Details

### Permissions Required

**Android (minSdkVersion: 26, targetSdkVersion: 35)**
- `android.permission.CAMERA` - Required for face detection to track when you're looking at the screen

**iOS**
- `NSCameraUsageDescription` - "This app needs camera access to detect your face and track eye contact time."

### Third-Party Libraries and SDKs

The app uses the following third-party services and libraries:

- **React Native (0.81.5)** - Mobile app framework
- **Expo (~54.0.20)** - Development and build platform
- **React Native Vision Camera (^4.7.2)** - Camera interface
- **React Native Vision Camera Face Detector (^1.9.1)** - Face detection using ML Kit
- **AsyncStorage (^2.2.0)** - Local data storage
- **Cloudflare D1 & Workers** - Backend database and API

All face detection processing happens on-device. No data from these libraries is sent to third parties except as described in this policy.

## Contact Us

If you have any questions, concerns, or requests regarding this Privacy Policy or your data, please contact us at:

**Email**: [Your contact email - to be added]
**App Package**: com.rawdog.app
**Privacy Policy URL**: [This page URL]

We will respond to all privacy requests within 30 days.

---

## Summary (Quick Reference)

**What we collect and store online:**
- Username
- Scores and timestamps
- Device ID (for username uniqueness)

**What we DON'T collect or store:**
- Facial recognition data (processed locally only, never transmitted)
- Personal details (email, phone, real name)
- Location data
- Camera images or video
- Usage analytics
- Device information beyond device ID

**How we use it:**
- Display your username and score on the global leaderboard
- Prevent duplicate usernames (one per device)
- That's it!

**Your privacy matters to us:**
- All face detection happens on your device and stays on your device
- No biometric data leaves your phone
- Camera is used only for local head pose detection
- You can request data deletion at any time

**Platform:** Available on Android (minSDK 26+)
**Package:** com.rawdog.app
