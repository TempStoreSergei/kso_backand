from typing import TYPE_CHECKING

from fastapi import Depends

from modules.cash_system.DTO.status_system_response_dto import BillAcceptorStatusResponseDTO, \
    BillDispenserStatusResponseDTO, StatusSystemResponseDTO
from api.dependencies.get_current_user import get_current_user
from api.dependencies.redis_connection import get_redis, pubsub_command_util
from modules.cash_system.configs.settings import cash_system_settings

if TYPE_CHECKING:
    from api.models.auth_models import User
    from redis.asyncio import Redis


async def status_system(
    user: "User" = Depends(get_current_user),
    redis: "Redis" = Depends(get_redis),
):
    command_bill_acceptor_status = {'command': 'bill_acceptor_status'}
    bill_acceptor_status = await pubsub_command_util(
        redis, cash_system_settings.PAYMENT_SYSTEM_CASH_CHANNEL, command_bill_acceptor_status
    )

    command_bill_dispenser_status = {'command': 'bill_dispenser_status'}
    bill_dispenser_status = await pubsub_command_util(
        redis, cash_system_settings.PAYMENT_SYSTEM_CASH_CHANNEL, command_bill_dispenser_status
    )

    return StatusSystemResponseDTO(
        bill_acceptor=BillAcceptorStatusResponseDTO(
            max_bill_count=bill_acceptor_status.get('data').get('max_bill_count'),
            bill_count=bill_acceptor_status.get('data').get('bill_count'),
        ) if bill_acceptor_status.get('success') else None,
        bill_dispenser=BillDispenserStatusResponseDTO(
            upper_box_value=bill_dispenser_status.get('data').get('upper_box_value'),
            lower_box_value=bill_dispenser_status.get('data').get('lower_box_value'),
            upper_box_count=bill_dispenser_status.get('data').get('upper_box_count'),
            lower_box_count=bill_dispenser_status.get('data').get('lower_box_count'),
        ) if bill_dispenser_status.get('success') else None,
        detail=f'{bill_acceptor_status.get('message')} | {bill_dispenser_status.get('message')}',
    )
