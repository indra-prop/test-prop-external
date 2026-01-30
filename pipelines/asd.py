with DAG():
    OrchestrationSource_1 = SourceTask(
        task_id = "OrchestrationSource_1", 
        component = "OrchestrationSource", 
        kind = "S3Source", 
        connector = Connection(kind = "s3", id = ""), 
        isNew = True, 
        format = CSVFormat(
          allowLazyQuotes = False, 
          allowEmptyColumnNames = True, 
          separator = ",", 
          nullValue = "", 
          encoding = "UTF-8", 
          header = True
        ), 
        fileOperationProperties = {"fileLoadingType" : "filepath", "includeFileNameColumn" : True}
    )
    OrchestrationSource_1 = Task(
        task_id = "OrchestrationSource_1", 
        component = "Dataset", 
        label = "OrchestrationSource_1", 
        table = {"name" : "{{ prophecy_tmp_source('asd', 'OrchestrationSource_1') }}", "sourceType" : "UnreferencedSource"}
    )
    asd__Aggregate_0 = Task(task_id = "asd__Aggregate_0", component = "Model", modelName = "asd__Aggregate_0")
    OrchestrationSource_1.out >> OrchestrationSource_1.input_port_0
    OrchestrationSource_1.output_port_0 >> asd__Aggregate_0.in_0
