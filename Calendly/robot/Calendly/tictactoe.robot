*** Settings ***
Documentation   Validates winning scenarios samples in TicTacToe
Library     Selenium2Library
Resource    robot/Calendly/resources/Calendly.robot 
Suite Setup     Open Browser    ${URL}   ${BROWSER}
Suite Teardown  Close All Browsers


*** Variables ***
${URL}              https://codepen.io/CalendlyQA/full/KKPQLmV
${BROWSER}          Chrome

${table_field}      css=form[name=f]
${button}           css=input[name=q]
${search_term}      Lambdatest

*** Test Cases ***
Player X Win
    Wait Until Element Is Visible  ${table_field}
    Wait Until Element Is Visible  ${button}
    Input Text      ${search_query}   ${EMPTY}
    Input Text      ${search_query}   ${search_term}
    Submit Form

Player O Win

Cat Does Not Trigger Alert