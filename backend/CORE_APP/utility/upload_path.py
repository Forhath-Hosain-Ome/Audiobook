def upload_to_dir(instance, filename):
    for field in instance._meta.fields:
        value = getattr(instance, field.name, None)
        if hasattr(value, 'name') and value.name and filename in value.name:
            field_name = field.name
            break
    else:
        field_name = 'unknown_field'
    title = getattr(instance, 'title', None)
    return f"{field_name}/{title}/{filename}"

