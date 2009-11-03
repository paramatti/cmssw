#ifndef __Validation_RecoParticleFlow_TH2Analyzer__
#define __Validation_RecoParticleFlow_TH2Analyzer__

#include <vector>

#include <TObject.h>

class TH2;
class TH1D;
class TH2D;

class TH2Analyzer : public TObject {

 public:
  TH2Analyzer( const TH2* h, int rebin=1) : 
    hist2D_(h), 
    rebinnedHist2D_(0),
    average_(0),
    RMS_(0),
    sigmaGauss_(0),
    meanXslice_(0) {
    Eval(rebin);
  }

  TH2Analyzer( const TH2* h, const int binxmin, const int binxmax, const int rebin) : 
    hist2D_(h), 
    rebinnedHist2D_(0),
    average_(0),
    RMS_(0),
    sigmaGauss_(0),
    meanXslice_(0) {
    Eval(rebin, binxmin, binxmax);
  } 

  ~TH2Analyzer() {Reset(); }

  void Reset();

  void SetHisto( const TH2* h ) {hist2D_ = h;}

  void Eval(const int rebinFactor);
  void Eval(const int rebinFactor, const int binxmin, const int binxmax);
  
  TH1D* Average() { return average_; }
  TH1D* RMS() { return RMS_; }
  TH1D* SigmaGauss() { return sigmaGauss_; }
  TH1D* MeanX() { return meanXslice_; }

 private:

  void ProcessSlices(  const TH2D* histo );
  void ProcessSlice(const int i, TH1D* histo ) const;

  const TH2* hist2D_;
  TH2D*      rebinnedHist2D_;
  TH1D*      average_;
  TH1D*      RMS_;
  TH1D*      sigmaGauss_;
  TH1D*      meanXslice_;

  //std::vector< TH1D* > parameters_; // if we are not fitting with a gauss function

};

#endif 
