from bert import binding, utils, constants

@binding.follow('noop')
def create_data():
    work_queue, done_queue, ologger = utils.comm_binders(create_data)

    for idx in range(0, 100):
        done_queue.put({
            'idx': idx
        })

@binding.follow(create_data, pipeline_type=constants.PipelineType.CONCURRENT)
def calculate_data():
    import math

    work_queue, done_queue, ologger = utils.comm_binders(calculate_data)

    for details in work_queue:
        details['calculated-result'] = math.pow(details['idx'], 2)
        done_queue.put(details)

@binding.follow(calculate_data, pipeline_type=constants.PipelineType.CONCURRENT)
def variation():
    work_queue, done_queue, ologger = utils.comm_binders(variation)

    for details in work_queue:
        for key, value in details.items():
            ologger.info(f'Key[{key}], Value[{value}], Alteration[{value % 5}]')

