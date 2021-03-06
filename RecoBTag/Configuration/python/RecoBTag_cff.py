import FWCore.ParameterSet.Config as cms

# define the b-tag squences for offline reconstruction
from RecoBTag.SoftLepton.softLepton_cff import *
from RecoBTag.ImpactParameter.impactParameter_cff import *
from RecoBTag.SecondaryVertex.secondaryVertex_cff import *
from RecoBTau.JetTagComputer.combinedMVA_cff import *
from RecoVertex.AdaptiveVertexFinder.inclusiveVertexing_cff import *

legacyBTagging = cms.Sequence(
    (
      # impact parameters and IP-only algorithms
      impactParameterTagInfos *
      ( trackCountingHighEffBJetTags +
        trackCountingHighPurBJetTags +
        jetProbabilityBJetTags +
        jetBProbabilityBJetTags +

        # SV tag infos depending on IP tag infos, and SV (+IP) based algos
        secondaryVertexTagInfos *
        ( simpleSecondaryVertexHighEffBJetTags +
          simpleSecondaryVertexHighPurBJetTags +
          combinedSecondaryVertexBJetTags
        )
        + inclusiveSecondaryVertexFinderTagInfos *
        combinedInclusiveSecondaryVertexV2BJetTags

        + ghostTrackVertexTagInfos *
        ghostTrackBJetTags
      ) +

      # soft lepton tag infos and algos
      softPFMuonsTagInfos *
      softPFMuonBJetTags
      + softPFElectronsTagInfos *
      softPFElectronBJetTags
    )

    # overall combined taggers
    * combinedMVABJetTags
)

# new candidate-based fwk, with PF inputs
pfBTagging = cms.Sequence(
    (
      # impact parameters and IP-only algorithms
      pfImpactParameterTagInfos *
      ( pfTrackCountingHighEffBJetTags +
        pfTrackCountingHighPurBJetTags +
        pfJetProbabilityBJetTags +
        pfJetBProbabilityBJetTags +

        # SV tag infos depending on IP tag infos, and SV (+IP) based algos
        pfSecondaryVertexTagInfos *
        ( pfSimpleSecondaryVertexHighEffBJetTags +
          pfSimpleSecondaryVertexHighPurBJetTags +
          pfCombinedSecondaryVertexBJetTags
        )
        + inclusiveCandidateVertexing *
        pfInclusiveSecondaryVertexFinderTagInfos *
        pfCombinedInclusiveSecondaryVertexV2BJetTags

      ) +

      # soft lepton tag infos and algos
      softPFMuonsTagInfos *
      softPFMuonBJetTags
      + softPFElectronsTagInfos *
      softPFElectronBJetTags
    ) *

    # overall combined taggers
    ( #CSV + soft-lepton + jet probability discriminators combined
      pfCombinedMVABJetTags

      #CSV + soft-lepton variables combined (btagger)
      + pfCombinedSecondaryVertexSoftLeptonBJetTags   
    )
)

# new candidate-based ctagging sequence, requires its own IVF vertices (relaxed IVF reconstruction cuts) 
# but IP and soft-lepton taginfos from btagging sequence can be recycled
pfCTagging = cms.Sequence(
    ( inclusiveCandidateVertexingCtagL *
      pfInclusiveSecondaryVertexFinderCtagLTagInfos
    ) *

    # CSV + soft-lepton variables combined (ctagger optimized for c vs dusg)
    pfCombinedSecondaryVertexSoftLeptonCtagLJetTags
)

btagging = legacyBTagging + pfBTagging #* pfCTagging
