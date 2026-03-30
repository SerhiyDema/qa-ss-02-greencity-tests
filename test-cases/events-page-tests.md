# **Test Cases: Events and Registration Module**

**Project:** GreenCity

**Testing Object:** Events Page

### **Test Case ID: gc-01**

**Summary:** Verify successful user registration with valid data

**Priority:** Critical

**Preconditions:** 1\. User is on the "Registration" modal window. 2\. User does not have an existing account with the provided email.

| Steps | Test Step | Test Data | Expected result |
| :---- | :---- | :---- | :---- |
| 1 | Enter a valid email address | sergey.dema@gmail.com | The field is filled without errors. |
| 2 | Enter a valid user name | Сергій Д | The field is filled without errors. |
| 3 | Enter a valid password (min 8 chars, 1 capital, 1 digit, 1 special char) | TestTest\#26 | Password is hidden; complexity requirements are met. |
| 4 | Re-enter the same password in "Confirm password" field | TestTest\#26 | Field matches the password field. |
| 5 | Click the "Register" button | \- | User is successfully registered; a success message or redirect occurs. |

### **Test Case ID: gc-02**

**Summary:** Verify that an authorized user can successfully join an event

**Priority:** High

**Preconditions:** 1\. User is logged into the system. 2\. User is on the "Events" page. 3\. An active event card is visible.

| Steps | Test Step | Test Data | Expected result |
| :---- | :---- | :---- | :---- |
| 1 | Locate the event card "Глобальний еко-вебінар 2026" | \- | The card is displayed with the "Join event" button. |
| 2 | Click the "Join event" (Приєднатися до події) button | \- | The button state changes to "Cancel participation"; user is added to the participants list. |

### **Test Case ID: gc-03**

**Summary:** Verify restriction of multiple likes/dislikes on an event

**Priority:** Medium

**Preconditions:** 1\. User is logged into the system. 2\. User is on the "Events" page.

| Steps | Test Step | Test Data | Expected result |
| :---- | :---- | :---- | :---- |
| 1 | Click the "Like" icon on an event card | \- | The like counter increases by 1\. |
| 2 | Click the "Like" icon again on the same event card | \- | The system should either toggle (remove like) or restrict further likes. |
| 3 | Rapidly click "Like" and "Dislike" multiple times | \- | The system should not allow infinite clicking/spamming; the counter should stay consistent. |

