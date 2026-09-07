---
name: observability
description: Designs logs, metrics, traces, correlation, health signals, SLO-oriented telemetry and operational diagnostics. Use for production-facing backend changes, incidents, distributed flows, background jobs or when defining how failures will be detected and diagnosed.
---


# Observability

Instrument for decisions and diagnosis, not log volume.

## Signals

- Logs: structured event/context detail.
- Metrics: aggregatable health/volume/latency/error signals.
- Traces: causal path across components.

## Rules

- propagate correlation/trace context across boundaries;
- never log secrets or unnecessary sensitive data;
- use stable event names/fields where dashboards/alerts depend on them;
- distinguish expected business rejections from system errors;
- instrument retries, queue lag, dependency failures and saturation where relevant;
- define health checks that reflect actual serving readiness without causing cascading load;
- connect important requirements/SLOs to measurable signals.

An operationally critical feature is incomplete if a severe failure would be invisible in production.
