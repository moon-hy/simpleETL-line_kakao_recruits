from extract.extractor import LineExtractor, KakaoExtractor
from transform.transformer import LineTransformer, KakaoTransformer
from load.loader import Loader
from job.etl_job import Pipeline

if __name__ == '__main__':
    loader = Loader()

    line_extractor = LineExtractor()
    line_transformer = LineTransformer()

    line_pipeline = Pipeline(line_extractor, line_transformer, loader)
    line_pipeline.run()

    kakao_extractor = KakaoExtractor()
    kakao_transformer = KakaoTransformer()

    kakao_pipeline = Pipeline(kakao_extractor, kakao_transformer, loader)
    kakao_pipeline.run()
