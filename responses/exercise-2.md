# Exercise 2

## Business Process Description

The business process is for climbers entering the gym. All climbers enter the gym in the same enterance. There will be 2 queues: new members and current members. 

The new members of the gym will need to queue on the representative line. The new members line enables the new climber to sign the wavier, purchase a day pass, become a new member and renew membership as well as resolve any issues with the current membership. Upon completing this process the climber will be able to enter the gym.

The current members of the gym have a pass they can use the self check-in queue. The check-in queue has multiple scanners enabling members to scan their pass. The scanner will project either a green light or red light. The green light the climber can immediately enter the gym. If the red light appears, the climber will need to join the new climber line. 



## Fact Table

Number of checkin by member
How long have the member been part of the gym?
Total Spent on the gym by member
When does the gym receive the most traffic?
Number of active memberships

| Column Name | Type | Description |
| --- | --- | --- |
| example | varchar | some text here |

Checkin By Member
member_id varchar member info
Count(DISTINCT datetime_checkin) INT count of the datetime the member has checkedin
SUM(Price) double sum of the priced of the membershipship the member has spent


Gym Receiving the most traffic
Checkin_DateTime datetime Date hour of the day the members checkedin
SUM(COUNT(distinct member_id))  

Active Memberships
member_id
card_pass_id
status


## Dimension

| Column Name | Type | Description |
| --- | --- | --- |
| example | varchar | some text here |

Member Table
member_id varchar unique identifer identifying the member
Name varchar name of the member
Address varchar address of the member
City varchar city of the member
State varchar state of the member
Zip Code int zip coode of the member
Gender varchar gender of the member
credit_card varchar payment info from the member

Pass Card Table (A member can have multiple cards)
pass_id varchar unique identifer of the pass enabling the member for self-checkin
member_id varchar unique identifer of the member
Date datetime time of card issued

Membership-Product Table
Product_ID varchar unique identifer identifying the product
Name varchar name of the product 
Description varchar describing the product/membership type
Category varchar what the product is categorize as
Price varchar price the of the membership

Member-Membership Table
member_id varchar member info
product_id varcahr product info
start_date datetime start date of the product
end_date datetime end date of the product
status varchar status of the member

Member Sign-In Table
member_sign_in_id varchar unique identifer of the event trigger
Check_Date_Time datetime check-in time
card_pass_id varchar card being used to checkin
member_id varchar member info
status varchar green-light (no issues with the member) or red-light(see front desk) 





