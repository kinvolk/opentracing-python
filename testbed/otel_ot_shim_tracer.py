import opentelemetry.ext.opentracing_shim as opentracingshim
from opentelemetry.sdk import trace
from opentelemetry.sdk.trace.export import SimpleExportSpanProcessor
from opentelemetry.sdk.trace.export.in_memory_span_exporter import (
    InMemorySpanExporter,
)

class MockTracer(opentracingshim.TracerShim):
    def __init__(self):
        oteltracer = trace.Tracer()
        super(MockTracer, self).__init__(oteltracer)
        exporter = InMemorySpanExporter()
        span_processor = SimpleExportSpanProcessor(exporter)
        oteltracer.add_span_processor(span_processor)

        self.exporter = exporter

    def finished_spans(self):
        return self.exporter.get_finished_spans()