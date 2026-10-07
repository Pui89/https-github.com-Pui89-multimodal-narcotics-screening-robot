from narcotics_platform import ScreeningPipeline

pipeline = ScreeningPipeline(threshold=0.60)
result = pipeline.screen([
    {'modality':'rgb','label':'unknown_substance','confidence':0.74,'quality':0.95},
    {'modality':'depth','label':'unknown_substance','confidence':0.68,'quality':0.90},
    {'modality':'thermal','label':'unknown_substance','confidence':0.52,'quality':0.80},
], sensor_quality=0.88, ood_score=0.15)

print(result)
print('Human review required:', result.requires_human_review)
