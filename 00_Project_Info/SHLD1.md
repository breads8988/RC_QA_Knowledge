# RepairCheck (RC) — Feature Tree (SHLD1)

> Function-only view: each feature that exists on both the end-user side (Web App, `wa_`) and the admin side (Web Portal, `wp_`) branches into its two variants. Features with only one side stay as a single node.

```mermaid
flowchart LR
    root([RC Features])

    root --> login[login]
    root --> registration[registration]
    root --> my_vehicle[my_vehicle]
    root --> user_management[user_management]
    root --> expert[expert]
    root --> expert_call_appointment[expert_call_appointment]
    root --> homepage[homepage]
    root --> tourguide[tourguide]
    root --> wp_advertisement[wp_advertisement]

    root --> lawyer[lawyer]
    lawyer --> wa_lawyer[wa_lawyer]
    lawyer --> wp_lawyer[wp_lawyer]

    root --> accident[accident]
    accident --> wa_accident_assistant[wa_accident_assistant]
    accident --> wa_my_accident[wa_my_accident]
    accident --> wp_accident_report[wp_accident_report]

    root --> workshop[workshop]
    workshop --> wa_workshop[wa_workshop]
    workshop --> wp_workshop[wp_workshop]

    root --> voucher[voucher]
    voucher --> wa_saved_voucher[wa_saved_voucher]
    voucher --> wp_user_voucher[wp_user_voucher]
```
