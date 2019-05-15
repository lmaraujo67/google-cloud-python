config = {
    "interfaces": {
        "google.cloud.phishingprotection.v1beta1.PhishingProtectionServiceV1Beta1": {
            "retry_codes": {"idempotent": ["UNAVAILABLE"], "non_idempotent": []},
            "retry_params": {
                "default": {
                    "initial_retry_delay_millis": 100,
                    "retry_delay_multiplier": 1.3,
                    "max_retry_delay_millis": 60000,
                    "initial_rpc_timeout_millis": 20000,
                    "rpc_timeout_multiplier": 1.0,
                    "max_rpc_timeout_millis": 20000,
                    "total_timeout_millis": 600000,
                }
            },
            "methods": {
                "ReportPhishing": {
                    "timeout_millis": 60000,
                    "retry_codes_name": "non_idempotent",
                    "retry_params_name": "default",
                }
            },
        }
    }
}