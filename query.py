import json
import weaviate

client = weaviate.Client("http://epsilon-it.utu.fi/qa-fi")

ask = {
    "question": "Mitä ASCII sisältää?",
    "rerank": "true"
}

result = (
    client.query
    .get("Article", ["title", "_additional {answer {hasAnswer certainty result} }"])
    .with_ask(ask)
    .with_limit(3)
    .do()
)

pretty = json.dumps(result, indent=2, ensure_ascii=False)
print(pretty)
