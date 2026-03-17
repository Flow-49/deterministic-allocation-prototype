# Hydrocarbon Allocation & Deterministic Calculation Engine

This repository contains a functional prototype for an upstream hydrocarbon allocation system. As a First-Class Electrical & Electronic Engineer, I have designed this engine to prioritize mathematical rigor, auditability, and unit consistency—the three pillars of production accounting.

## Core Engineering Principles
Deterministic Execution: To prevent LLM hallucinations, all mathematical logic is handled by a dedicated Python module using the Decimal library for high-precision arithmetic.

Audit Trails: Every calculation step is logged with an "Allocation Factor" to ensure 0% data decay and 100% transparency for fiscal audits.

Uncertainty Propagation: The system is designed to account for measurement uncertainty in physical meters (GUM framework).

## Calculation Methods Implemented
Pro-rata Allocation: Distributing total fiscal readings back to individual wells based on their theoretical contribution ratios.

By-Difference Logic: Handling scenarios where a specific meter is offline or unmetered by subtracting known variables from the total system volume.

## AI Agent Integration (LLM Layer)
This engine is designed to be orchestrated by a LangChain/LangGraph agent.

The LLM's Role: To interpret production anomalies (e.g., "Why is Well A's pressure dropping?") and query the deterministic engine.

The Validation Layer: The LLM cannot perform the math; it can only request the Python engine to execute it and then translate the result for human reporting.

## Tech Stack
Language: Python 3.10+

Libraries: Decimal (Precision), Pint (Unit Consistency), Pytest (Logic Validation).

Architecture: Modular, API-ready, and container-friendly.
