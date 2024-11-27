#!/usr/bin/env python3
# 
# ArchiMate tool to extract PlantUML procedures from the file Archimate.puml.
#
# https://github.com/plantuml-stdlib/Archimate-PlantUML/blob/master/Archimate.puml
#
# This script helps us discover the PlantUML macros for elements.
#
# The current list of results in order from high-level to low-level:
#
# * Motivation_Stakeholder
# * Motivation_Driver
# * Motivation_Assessment
# * Motivation_Goal
# * Motivation_Outcome
# * Motivation_Principle
# * Motivation_Requirement
# * Motivation_Constraint
# * Motivation_Meaning
# * Motivation_Value
# * Strategy_Resource
# * Strategy_Capability
# * Strategy_CourseOfAction
# * Strategy_ValueStream
# * Business_Actor
# * Business_Role
# * Business_Collaboration
# * Business_Interface
# * Business_Process
# * Business_Function
# * Business_Interaction
# * Business_Event
# * Business_Service
# * Business_Object
# * Business_Contract
# * Business_Representation
# * Business_Product
# * Business_Location
# * Application_Component
# * Application_Collaboration
# * Application_Interface
# * Application_Function
# * Application_Interaction
# * Application_Process
# * Application_Event
# * Application_Service
# * Application_DataObject
# * Technology_Node
# * Technology_Device
# * Technology_SystemSoftware
# * Technology_Collaboration
# * Technology_Interface
# * Technology_Path
# * Technology_CommunicationNetwork
# * Technology_Function
# * Technology_Process
# * Technology_Interaction
# * Technology_Event
# * Technology_Service
# * Technology_Artifact
# * Physical_Equipment
# * Physical_Facility
# * Physical_DistributionNetwork
# * Physical_Material
# * Implementation_WorkPackage
# * Implementation_Deliverable
# * Implementation_Event
# * Implementation_Plateau
# * Implementation_Gap

import sys
import re

pattern = r"your_pattern_here"

for line in sys.stdin:
    if re.search(r"!unquoted procedure", line):
        line = re.sub(".*!unquoted procedure (.*)\(.*\n", r"\1", line)
        print(line)
        