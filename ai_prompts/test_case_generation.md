# AI-Assisted Test Case Generation Prompt

## Purpose
Generate an initial set of QA test scenarios from a user story. AI output is treated as a draft and must be reviewed by a human.

## Prompt
You are assisting a QA engineer. Given the requirement below, produce a structured list of:
1. happy-path scenarios
2. negative scenarios
3. boundary cases
4. data-quality cases
5. API validation cases
6. security/privacy considerations that are relevant to testing

Do not invent business rules that are not supported by the requirement. Mark assumptions explicitly.

Requirement:
> As a customer, I want to reset my password so that I can regain access to my account.

Return columns:
Test ID | Scenario | Preconditions | Test Data | Expected Result | Risk | Assumption
