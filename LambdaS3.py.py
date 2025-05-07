import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext

sc = SparkContext()
glueContext = GlueContext(sc)
args = getResolvedOptions(sys.argv, ["input_path", "output_path"])

# Read CSV
datasource = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [args["input_path"]]},
    format="csv",
    format_options={"withHeader": True}
)

# Write to Parquet
glueContext.write_dynamic_frame.from_options(
    frame=datasource,
    connection_type="s3",
    connection_options={"path": args["output_path"]},
    format="parquet"
)