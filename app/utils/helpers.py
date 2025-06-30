def normalize_topic(mqtt_topic: str) -> str:
    # hub/device1/data → device1/data
    parts = mqtt_topic.split("/")
    if len(parts) >= 3:
        return f"{parts[1]}/{parts[2]}"
    return mqtt_topic
