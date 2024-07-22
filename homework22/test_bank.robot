*** Settings ***
Library           bank_keywords.py
Library           BuiltIn
Library           OperatingSystem


*** Variables ***
${EXPECTED_AMOUNT_DEPOSIT_1}    12203.909614
${EXPECTED_AMOUNT_DEPOSIT_2}    18305.864421

*** Test Cases ***
Test Deposit 1
    [Documentation]    Test deposit method with deposit_1.
    ${bank}=    Create Bank    10
    ${deposit_1}=    Create Deposit    10000    2
    ${result}=    Deposit Money    ${bank}    ${deposit_1}
    Log Message    Testing deposit_1: expected ${EXPECTED_AMOUNT_DEPOSIT_1}, got ${result}
    Should Be Equal As Numbers    ${result}    ${EXPECTED_AMOUNT_DEPOSIT_1}    2
    Log Message    Successfully verified deposit calculation

Test Deposit 2
    [Documentation]    Test deposit method with deposit_2.
    ${bank}=    Create Bank    10
    ${deposit_2}=    Create Deposit    15000    2
    ${result}=    Deposit Money    ${bank}    ${deposit_2}
    Log Message    Testing deposit_2: expected ${EXPECTED_AMOUNT_DEPOSIT_2}, got ${result}
    Should Be Equal As Numbers    ${result}    ${EXPECTED_AMOUNT_DEPOSIT_2}    2
    Log Message    Successfully verified deposit calculation

Test Is Instance
    [Documentation]    Test if deposit_1 is an instance of Deposit.
    ${deposit_1}=    Create Deposit    10000    2
    Log Message    Starting test to verify if deposit_1 is an instance of Deposit.
    ${result}=    check_if_instance  ${deposit_1}
    Should Be True    ${result}
    Log Message    Successfully verified deposit_1 is an instance of Deposit


Test Deposit Total Sum
    [Documentation]    Test that the deposit amount is greater than the initial amount.
    ${bank}=    Create Bank    10
    ${deposit_1}=    Create Deposit    10000    2
    ${result}=    Deposit Money    ${bank}    ${deposit_1}
    Log Message    Starting test to verify that the deposit amount is greater than the initial amount.
    Should Be True    ${result} > ${deposit_1.amount}
    Log Message    Successfully verified that deposit result ${result} is greater than the initial amount ${deposit_1.amount}.

Test Deposit Is True
    [Documentation]    Test that the deposit method returns a truthy value.
    ${bank}=    Create Bank    10
    ${deposit_1}=    Create Deposit    10000    2
    ${result}=    Deposit Money    ${bank}    ${deposit_1}
    Log Message    Starting test to verify that deposit method returns a truthy value.
    Should Be True    ${result}
    Log Message    Successfully verified that deposit method returns a truthy value.

Test Deposit Amount Less
    [Documentation]    Test that the deposit amount is less than the bank's deposit result.
    ${bank}=    Create Bank    10
    ${deposit_1}=    Create Deposit    10000    2
    ${result}=    Deposit Money    ${bank}    ${deposit_1}
    ${initial_amount}=    Get Deposit Amount    ${deposit_1}
    Log Message    Starting test to verify that deposit amount is less than the bank's deposit result.
    Should Be True    ${initial_amount} < ${result}
    Log Message    Successfully verified that deposit amount ${initial_amount} is less than the bank's deposit result ${result}.

*** Keywords ***
Get Deposit Amount
    [Arguments]    ${deposit}
    RETURN    ${deposit.amount}
