require 'rails_helper'

RSpec.describe Skin, type: :model do
  subject { Skin.create(api_id: 1) }

  it { should serialize(:flags) }
  it { should serialize(:restrictions) }

  describe 'associations' do
    it { should belong_to(:collection).optional }

    it 'updates its collection when :unlocked is changed' do
      subject.create_collection
      expect(subject.collection.unlocked).to eq(false)
      subject.update(unlocked: true)
      expect(subject.collection.unlocked).to eq(true)
    end
  end

  describe 'validations' do
    it { should validate_presence_of(:api_id) }
  end
end
