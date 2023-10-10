# Auto generated configuration file
# using: 
# Revision: 1.381.2.28 
# Source: /local/reps/CMSSW/CMSSW/Configuration/PyReleaseValidation/python/ConfigBuilder.py,v 
# with command line options: step3 --data --conditions FT_R_53_LV5::All -s RAW2DIGI,RECO --scenario HeavyIons --datatier GEN-SIM-RECO --eventcontent RECODEBUG -n 100 --repacked --no_exec
import FWCore.ParameterSet.Config as cms

process = cms.Process('RECO')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContentHeavyIons_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.load('Configuration.StandardSequences.ReconstructionHeavyIons_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

# Input source
process.source = cms.Source("PoolSource",
                            secondaryFileNames = cms.untracked.vstring(),
                            fileNames = cms.untracked.vstring('/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/066/14B65DE8-9512-E111-AA9F-BCAEC53296F6.root')
                            )

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.381.2.28 $'),
    annotation = cms.untracked.string('step3 nevts:100'),
    name = cms.untracked.string('PyReleaseValidation')
)

# Output definition

process.RECODEBUGoutput = cms.OutputModule("PoolOutputModule",
                                           splitLevel = cms.untracked.int32(0),
                                           eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
                                           outputCommands = process.RECODEBUGEventContent.outputCommands,
                                           fileName = cms.untracked.string('DATA_MinBias_RECO.root'),
                                           dataset = cms.untracked.PSet(
    filterName = cms.untracked.string('MinBiasCollEvtSel'),
    dataTier = cms.untracked.string('GEN-SIM-RECO')
    ),
                                           SelectEvents = cms.untracked.PSet(
    SelectEvents = cms.vstring('filter_step')
    )
                                           
                                           )

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'GR_R_53_LV6::All', '')

process.load("FWCore.Modules.preScaler_cfi")
process.preScaler.prescaleFactor = 20

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.preScaler*process.RawToDigi)
process.reconstruction_step = cms.Path(process.preScaler*process.reconstructionHeavyIons)

process.endjob_step = cms.EndPath(process.endOfProcess)
process.RECODEBUGoutput_step = cms.EndPath(process.RECODEBUGoutput)
process.filter_step = cms.Path(process.preScaler)

# Schedule definition
process.schedule = cms.Schedule(process.filter_step,process.raw2digi_step,process.reconstruction_step,process.endjob_step,process.RECODEBUGoutput_step)

from Configuration.PyReleaseValidation.ConfigBuilder import MassReplaceInputTag
MassReplaceInputTag(process)

process.SimpleMemoryCheck=cms.Service("SimpleMemoryCheck",
                                      oncePerEventMode=cms.untracked.bool(False))

process.Timing=cms.Service("Timing",
                           useJobReport = cms.untracked.bool(True)
                           )


# Load Beamspot
from CondCore.DBCommon.CondDBSetup_cfi import *
process.beamspot = cms.ESSource("PoolDBESSource",CondDBSetup,
                                toGet = cms.VPSet(cms.PSet( record = cms.string('BeamSpotObjectsRcd'),
                                                            tag= cms.string('BeamSpotObjects_2009_LumiBased_SigmaZ_v27_offline')
                                                            )),
                                connect =cms.string('sqlite_file:BeamSpotObjects_2009_LumiBased_SigmaZ_v27_offline.db')
                                )
process.es_prefer_beamspot = cms.ESPrefer("PoolDBESSource","beamspot")


