#! /usr/bin/env python
# -*- coding: utf-8 -*-
####################
# Hue Lights Indigo Plugin
#	This file is imported into the main plugin.py file.

### CONSTANTS ###

# List of compatible device IDs that may be associated with a Hue hub.
#
# Philips Hue Color and Ambiance Lights
# LCT001	=	Hue bulb (color gamut B)
# LCT002	=	Hue Downlight/Spot BR30 bulb (color gamut B)
# LCT003	=	Hue Spot Light GU10 bulb (color gamut B)
# LCT007	=	Hue bulb (800 lumen version, color gamut B)
# LCT010	=	Hue bulb (A19 version 3, color gamut C)
# LCT011	=	Hue bulb (BR30 version 3, color gamut C)
# LCT012	=	Hue bulb (E14 color candle, color gamut C)
# LCT014	=	Hue bulb (alternate A19 version 3, color gamut C)
# LCT015	=	Hue bulb (alternate A19 version 3, color gamut C)
# LCT016	=	Hue bulb (alternate A19 version 3, color gamut C)
#
# Philips LivingColors and Other Color Lights (color gamut A)
# LLC001	=	LivingColors light (generic)
# LLC005	=	LivingColors Gen3 Bloom/Aura
# LLC006	=	LivingColors Gen3 Iris
# LLC007	=	LivingColors Gen3 Bloom/Aura
# LLC010	=	LivingColors Iris (Europe)
# LLC011	=	Bloom (European?)
# LLC012	=	Bloom
# LLC013	=	Disney StoryLight
# LLC014	=	LivingColors Gen3 Aura
# LLC020	=	Hue Go
#
# Philips Luminaire Light Modules
# LLM001	=	Hue Luminaire Color Light Module (color gamut B)
# LLM010	=	Hue Color Temperature Module (2200K - 6500K)
# LLM011	=	Hue Color Temperature Module (2200K - 6500K)
# LLM012	=	Hue Color Temperature Module (2200K - 6500K)
#
# Philips LightStrips
# LST001	=	LED LightStrip (color gamut A)
# LST002	=	LED LightStrip Plus (color gamut C)
#
# Philips Ambiance Lights (color temperature only)
# LTW001	=	Hue A19 White Ambiance bulb
# LTC001	=	Hue Ambiance Ceiling
# LTC002	=	Hue Ambiance Ceiling
# LTC003	=	Hue Ambiance Ceiling
# LTC004	=	Hue Ambiance Ceiling
# LTF001	=	Hue Ambiance Ceiling
# LTF002	=	Hue Ambiance Ceiling
# LTD001	=	Hue Ambiance Ceiling
# LTD002	=	Hue Ambiance Ceiling
# LTW004	=	Hue A19 White Ambiance bulb
# LTW010	=	Hue A19 White Ambiance bulb
# LTW011	=	Hue BR13 White Ambiance bulb
# LTW012	=	Hue Ambiance Candle E14 bulb
# LTW013	=	Hue Ambiance Spot GU10 spotlight bulb
# LTW014	=	Hue Ambiance Spot GU10 spotlight bulb
# LTW015	=	Hue A19 White Ambiance bulb
# LTP001	=	Hue Ambiance Pendant light
# LTP002	=	Hue Ambiance Pendant light
# LTP003	=	Hue Ambiance Pendant light
# LTP004	=	Hue Ambiance Pendant light
# LTP005	=	Hue Ambiance Pendant light
# LTD003	=	Hue Ambiance Pendant light
# LFF001	=	Hue Ambiance Floor light
# LTT001	=	Hue Ambiance Table light
# LDT001	=	Hue Ambiance Downlight
#
# Philips LivingWhites (Dimming Only) Lights
# LWB001	=	LivingWhites bulb
# LWB003	=	LivingWhites bulb
# LWB004	=	Hue A19 Lux
# LWB006	=	Hue White A19 extension bulb
# LWB007	=	Hue Lux (alternate version)
# LWB010	=	Hue White (version 2)
# LWB014	=	Hue White (version 3)
# LDF001	=	Hue White Ceiling
# LDF002	=	Hue White Wall Washer
# LDD001	=	Hue White Table
# LDD002	=	Hue White Floor
# MWM001	=	Hue White 1-10V
#
# Philips LivingWhites Light Socket
# LWL001	=	LivingWhites light socket
#
# Philips Hue Beyond Multisource Lights (used with LLM001 or individually).
# HBL001	=	Hue Beyond Table
# HBL002	=	Hue Beyond Pendant
# HBL003	=	Hue Beyond Ceiling
# HEL001	=	Hue Entity Table
# HEL002	=	Hue Entity Pendant
# HIL001	=	Hue Impulse Table
# HIL002	=	Hue Impulse Pendant
#
# Philips Hue Phoenix Lights (used with the LLM010, LLM011 and LLM012, or individually).
# HML001	=	Phoenix Centerpiece
# HML002	=	Phoenix Ceiling
# HML003	=	Phoenix Pendant
# HML004	=	Phoenix Wall
# HML005	=	Phoenix Table
# HML006	=	Phoenix Downlight
#
# Philips Hue Motion Sensors
# SML001	=	Hue Motion Sensor (multi-sensor with presense, illumination and temperature)
#
# 3rd Party (Non-Philips) ZigBee Lights
# ZLL Light	=	Generic ZigBee Light (e.g. GE Link LEDs)
# FLS-PP3	=	Dresden Elektronik FLS-PP lp LED light strip, color LED segment
# FLS-PP3 White	=	Dresden Elektronik FLS-PP lp LED light strip, white light segment
# Classic A60 TW	=	Osram Lightify A60 Tunable White bulb (color temp. only)
# Classic A60 RGBW	=	Osram Lightify A60 RGBW bulb (extended color bulb)
# Flex RGBW	=	Osram Lightify Flex RGBW light strip (extended color light)
# PAR16 50 TW	=	Osram PAR-16 50W equivalent Tunable White bulb (color temp. only)
# TRADFRI bulb E26 opal 1000lm	=	IKEA dimmable 1000 lumen E26 light
# TRADFRI bulb E27 opal 1000lm	=	IKEA dimmable 1000 lumen E27 light
# RS 128 T	=	Innr RS-128T GU10 color temperature lights


### LIGHTS ###
##############
# Compatible Hue bulb devices (Color and Color Temperature)
kHueBulbDeviceIDs = ['LCT001', 'LCT002', 'LCT003', 'LCT007', 'LCT010', 'LCT011', 'LCT012', 'LCT014', 'LCT015', 'LCT016', 'LLM001', 'HBL001', 'HBL002', 'HBL003', 'HEL001', 'HEL002,' 'HIL001', 'HIL002', 'FLS-PP3', 'Classic A60 RGBW']
# Compatible LivingColors devices (Color only)
kLivingColorsDeviceIDs = ['LLC001', 'LLC005', 'LLC006', 'LLC007', 'LLC010', 'LLC011', 'LLC012', 'LLC013', 'LLC014', 'LLC020']
# Compatible Ambiance devices (Color Temperature only)
kAmbianceDeviceIDs = ['LLM010', 'LLM011', 'LLM012', 'LTW001', 'LTC001', 'LTC003', 'LTC002', 'LTC003', 'LTW004', 'LTW010', 'LTW011', 'LTW012', 'LTW013', 'LTW014', 'LTW015', 'LTF001', 'LTF002', 'LTD001', 'LTD002', 'LTP001', 'LTP002', 'LTP003', 'LTP004', 'LTP005', 'LTD003', 'LFF001', 'LTT001', 'LDT001', 'HML001', 'HML002', 'HML003', 'HML004', 'HML005', 'HML006', 'Classic A60 TW', 'PAR16 50 TW', 'RS 128 T']
# Compatible LightStrips devices. (Color only on LST001. Color and Color Temperature on others)
kLightStripsDeviceIDs = ['LST001', 'LST002', 'Flex RGBW']
# Compatible LivingWhites devices. (Dimming only.  No color change of any kind)
kLivingWhitesDeviceIDs = ['LWB001', 'LWB003', 'LWB004', 'LWB006', 'LWB007', 'LWB010', 'LWB014', 'LWL001', 'LDF001', 'LDF002', 'LDD001', 'LDD002', 'MWM001', 'ZLL Light', 'FLS-PP3 White', 'TRADFRI bulb E26 opal 1000lm', 'TRADFRI bulb E27 opal 1000lm']
# All compatible light devices
kCompatibleDeviceIDs = kHueBulbDeviceIDs + kAmbianceDeviceIDs + kLivingColorsDeviceIDs + kLightStripsDeviceIDs + kLivingWhitesDeviceIDs


### SENSORS ###
###############
# Supported Sensor Types
kSupportedSensorTypes = ['ZLLPresence', 'ZLLTemperature', 'ZLLLightLevel']
#
# Specific Sensor Models...
# Compatible motion sensors
kMotionSensorDeviceIDs = ['SML001']
# Compatible light sensors
kLightSensorDeviceIDs = ['SML001']
# Compatible temperature sensors
kTemperatureSensorDeviceIDs = ['SML001']


### Other Constants ###
#######################
# All Light Device Type IDs.
kLightDeviceTypeIDs = ['hueBulb', 'hueAmbiance', 'hueLightStrips', 'hueLivingColorsBloom', 'hueLivingWhites']
# All Group Device Type IDs.
kGroupDeviceTypeIDs = ['hueGroup']
# All Motion Sensor Type IDs.
kMotionSensorTypeIDs = ['hueMotionSensor']
# All Temperature Sensor Type IDs.
kTemperatureSensorTypeIDs = ['hueMotionTemperatureSensor']
# All Light Sensor Type IDs.
kLightSensorTypeIDs = ['hueMotionLightSensor']
