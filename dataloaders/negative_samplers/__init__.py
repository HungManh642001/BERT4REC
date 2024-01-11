from .random import RandomNegatvieSampler
from .popular import PopularNegativeSampler

NEGATIVE_SAMPLERS = {
    PopularNegativeSampler.code(): PopularNegativeSampler,
    RandomNegatvieSampler.code(): RandomNegatvieSampler,
}

def negative_sample_factory(code, train, val, test, user_count, item_count, sample_size, seed, save_folder):
    negative_sampler = NEGATIVE_SAMPLERS[code]
    return negative_sampler(train, val, test, user_count, item_count, sample_size, seed, save_folder)