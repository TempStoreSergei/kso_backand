async def payment_system_cash_commands(command_data, api):
    """Выполнение команды на основе полученной из pubsub"""
    command = command_data.get('command')
    command_id = command_data.get('command_id')
    data = command_data.get('data')
    response = {
        "command_id": command_id,
        "success": False,
        "message": None,
        "data": None
    }
    if command == 'init_devices':
        response_data = await api.init_devices()

    elif command == 'start_accepting_payment':
        target_amount = data.get("amount", 0)
        response_data = await api.start_accepting_payment(target_amount)

    elif command == 'stop_accepting_payment':
        response_data = await api.stop_accepting_payment()

    elif command == 'test_dispense_change':
        response_data = await api.test_dispense_change()

    elif command == 'bill_acceptor_set_max_bill_count':
        value = data.get('value')
        response_data = await api.bill_acceptor_set_max_bill_count(value)

    elif command == 'bill_acceptor_reset_bill_count':
        response_data = await api.bill_acceptor_reset_bill_count()

    elif command == 'bill_acceptor_status':
        response_data = await api.bill_acceptor_status()

    elif command == 'set_bill_dispenser_lvl':
        upper_lvl = data.get('upper_lvl') // 100
        lower_lvl = data.get('lower_lvl') // 100
        response_data = await api.set_bill_dispenser_lvl(upper_lvl, lower_lvl)

    elif command == 'set_bill_dispenser_count':
        upper_count = data.get('upper_count')
        lower_count = data.get('lower_count')
        response_data = await api.set_bill_dispenser_count(upper_count, lower_count)

    elif command == 'bill_dispenser_status':
        response_data = await api.bill_dispenser_status()

    elif command == 'bill_dispenser_reset_bill_count':
        response_data = await api.bill_dispenser_reset_bill_count()

    else:
        response_data = {}

    response.update(response_data)
    return response
